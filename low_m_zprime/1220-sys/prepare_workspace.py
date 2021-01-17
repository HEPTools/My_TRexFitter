import pathlib
from shutil import copyfile

from workspace_const import p4_sys_names

with open("config_template.config", "r") as f:
    config_temp = f.read()

with open("config_template_wt_sys_module.config", "r") as f:
    config_wt_sys_temp = f.read()

with open("config_template_p4_sys_module.config", "r") as f:
    config_p4_sys_temp = f.read()

# parameters
# nominal_ntuple_dir = "/data/zprime/ntuples_fit/fit_ntup_1201_high/run2"
fit_ntup_dir = "/data/zprime/ntuples_fit/1220-sys"
mass_points_low = [5, 7, 9, 11, 13, 15, 17, 19, 23, 27, 31, 35, 39]
mass_points_high = [42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75]
dnn_cuts = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]


def get_mass_cut(mass):
    sigma_range = 3 * (-0.0202966 + 0.0190822 * mass)
    return (mass - sigma_range, mass + sigma_range)


for mass in mass_points_low + mass_points_high:
    if mass in mass_points_low:
        region = "low_mass"
        fit_var = "mz2"
    elif mass in mass_points_high:
        region = "high_mass"
        fit_var = "mz1"
    else:
        print("#### ERROR! Unknown mass!")
        exit(1)
    # prepare folders
    folder_path_stats = pathlib.Path(f"{region}_stats/m_{mass:02d}")
    folder_path_stats.mkdir(parents=True, exist_ok=True)
    folder_path = pathlib.Path(f"{region}_sys/m_{mass:02d}")
    folder_path.mkdir(parents=True, exist_ok=True)
    mass_cut_low, mass_cut_high = get_mass_cut(mass)
    for dnn_cut in dnn_cuts:
        dnn_label = f"{int(dnn_cut*100):02d}"

        # write config without sys
        new_config_stats = config_temp.format(
            p_fit_type="stats",
            p_mass=mass,
            p_fit_var=fit_var,
            p_ntuple_path=f"{fit_ntup_dir}/{region}/tree_NOMINAL/run2",
            p_mass_cut_low=mass_cut_low,
            p_mass_cut_high=mass_cut_high,
            p_dnn_cut=dnn_cut,
            p_dnn_cut_label=dnn_label,
            p_region=region,
        )
        config_name = f"m_{mass:03d}_dnn_p{dnn_label}_stats.config"
        with folder_path_stats.joinpath(config_name).open("w", encoding="utf-8") as f:
            f.write(new_config_stats)

        # prepare sys config
        # set nominal config
        new_config = config_temp.format(
            p_fit_type="sys",
            p_mass=mass,
            p_fit_var=fit_var,
            p_ntuple_path=f"{fit_ntup_dir}/{region}/tree_NOMINAL/run2",
            p_mass_cut_low=mass_cut_low,
            p_mass_cut_high=mass_cut_high,
            p_dnn_cut=dnn_cut,
            p_dnn_cut_label=dnn_label,
            p_region=region,
        )
        # add weight systematic config
        sys_config = ""
        config_wt_config = config_wt_sys_temp.format(
            p_mass=mass, p_region=region, p_qcd_var=fit_var,
        )
        sys_config += config_wt_config
        # add p4 systematic config
        for sys_name in p4_sys_names:
            ntuple_path_up_sig = f"{fit_ntup_dir}/{region}/tree_{sys_name}up/run2"
            ntuple_path_down_sig = f"{fit_ntup_dir}/{region}/tree_{sys_name}down/run2"
            # sig
            sys_entry = config_p4_sys_temp.format(
                p_sys_name=sys_name[5:],
                p_sample="Zprime",
                p_ntuple_path_up=ntuple_path_up_sig,
                p_ntuple_path_down=ntuple_path_down_sig,
                p_ntuple_files=f"sig_Zp{mass:03d}",
                p_weight_str="weight",
            )
            sys_config += sys_entry
            # bkg
            ntuple_path_up_bkg = f"{fit_ntup_dir}/{region}/tree_{sys_name}up/run2"
            ntuple_path_down_bkg = f"{fit_ntup_dir}/{region}/tree_{sys_name}down/run2"
            sys_entry = config_p4_sys_temp.format(
                p_sys_name=sys_name,
                p_sample="ZZ4l",
                p_ntuple_path_up=ntuple_path_up_bkg,
                p_ntuple_path_down=ntuple_path_down_bkg,
                p_ntuple_files="bkg_qcd",
                p_weight_str="weight",
            )
            sys_config += sys_entry
        new_config += sys_config
        # write config with sys
        config_name = f"m_{mass:03d}_dnn_p{dnn_label}_sys.config"
        with folder_path.joinpath(config_name).open("w", encoding="utf-8") as f:
            f.write(new_config)
    fit_script_name = "fit_all.sh"
    copyfile(f"./{fit_script_name}", folder_path_stats.joinpath(fit_script_name))
    copyfile(f"./{fit_script_name}", folder_path.joinpath(fit_script_name))

# prepare special m_42 fit mz2
mass = 42
folder_path_stats = pathlib.Path(f"high_mass_stats/m_42_mz2")
folder_path_stats.mkdir(parents=True, exist_ok=True)
folder_path = pathlib.Path(f"high_mass_sys/m_42_mz2")
folder_path.mkdir(parents=True, exist_ok=True)
mass_cut_low, mass_cut_high = get_mass_cut(mass)
for dnn_cut in dnn_cuts:
    dnn_label = f"{int(dnn_cut*100):02d}"

    # write config without sys
    new_config_stats = config_temp.format(
        p_fit_type="stats",
        p_mass=mass,
        p_fit_var="mz2",
        p_ntuple_path=f"{fit_ntup_dir}/{region}/tree_NOMINAL/run2",
        p_mass_cut_low=mass_cut_low,
        p_mass_cut_high=mass_cut_high,
        p_dnn_cut=dnn_cut,
        p_dnn_cut_label=dnn_label,
        p_region=region,
    )
    config_name = f"m_{mass:03d}_dnn_p{dnn_label}_stats.config"
    with folder_path_stats.joinpath(config_name).open("w", encoding="utf-8") as f:
        f.write(new_config_stats)

    # prepare config with sys
    # set nominal config
    new_config = config_temp.format(
        p_fit_type="sys",
        p_mass=mass,
        p_fit_var="mz2",
        p_ntuple_path=f"{fit_ntup_dir}/{region}/tree_NOMINAL/run2",
        p_mass_cut_low=mass_cut_low,
        p_mass_cut_high=mass_cut_high,
        p_dnn_cut=dnn_cut,
        p_dnn_cut_label=dnn_label,
        p_region=region,
    )
    # add weight systematic config
    sys_config = ""
    config_wt_config = config_wt_sys_temp.format(
        p_mass=mass, p_region=region, p_qcd_var="mz1",
    )
    sys_config += config_wt_config
    # add p4 systematic config
    for sys_name in p4_sys_names:
        # for sys_name in ["EG_RESOLUTION_ALL__1"]:
        ntuple_path_up_sig = f"{fit_ntup_dir}/{region}/tree_{sys_name}up/run2"
        ntuple_path_down_sig = f"{fit_ntup_dir}/{region}/tree_{sys_name}down/run2"
        # sig
        sys_entry = config_p4_sys_temp.format(
            p_sys_name=sys_name[5:],
            p_sample="Zprime",
            p_ntuple_path_up=ntuple_path_up_sig,
            p_ntuple_path_down=ntuple_path_down_sig,
            p_ntuple_files=f"sig_Zp{mass:03d}",
            p_weight_str="weight",
        )
        sys_config += sys_entry
        # bkg
        ntuple_path_up_bkg = f"{fit_ntup_dir}/{region}/tree_{sys_name}up/run2"
        ntuple_path_down_bkg = f"{fit_ntup_dir}/{region}/tree_{sys_name}down/run2"
        sys_entry = config_p4_sys_temp.format(
            p_sys_name=sys_name[5:],
            p_sample="ZZ4l",
            p_ntuple_path_up=ntuple_path_up_bkg,
            p_ntuple_path_down=ntuple_path_down_bkg,
            p_ntuple_files="bkg_qcd",
            p_weight_str="weight",
        )
        sys_config += sys_entry
    new_config += sys_config
    # write config with sys
    config_name = f"m_{mass:03d}_dnn_p{dnn_label}_sys.config"
    with folder_path.joinpath(config_name).open("w", encoding="utf-8") as f:
        f.write(new_config)
fit_script_name = "fit_all.sh"
copyfile(f"./{fit_script_name}", folder_path_stats.joinpath(fit_script_name))
copyfile(f"./{fit_script_name}", folder_path.joinpath(fit_script_name))


fit_script_name = "get_limits.py"
copyfile(f"./{fit_script_name}", pathlib.Path(f"low_mass_stats").joinpath(fit_script_name))
copyfile(f"./{fit_script_name}", pathlib.Path(f"low_mass_sys").joinpath(fit_script_name))
copyfile(f"./{fit_script_name}", pathlib.Path(f"high_mass_stats").joinpath(fit_script_name))
copyfile(f"./{fit_script_name}", pathlib.Path(f"high_mass_sys").joinpath(fit_script_name))
