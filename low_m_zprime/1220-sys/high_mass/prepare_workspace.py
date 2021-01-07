import pathlib
from shutil import copyfile

from workspace_const import p4_sys_names

with open("config_template.config", "r") as f:
    config_temp = f.read()

with open("config_template_p4_sys_module.config", "r") as f:
    config_p4_sys_temp = f.read()

# print(config_temp)

print("#" * 80)

new_config = config_temp.format(
    p_mass=42,
    p_ntuple_path="/data/zprime/ntuples_fit/fit_ntup_1201_high/run2",
    p_mass_cut_low=40,
    p_mass_cut_high=44,
    p_dnn_cut=0.5,
    p_dnn_cut_label=f"{int(0.5*100):02d}",
)

#print(new_config)

print("#" * 80)

# parameters
nominal_ntuple_dir = "/data/zprime/ntuples_fit/fit_ntup_1201_high/run2"
mass_points = [42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75]
mass_cuts_dict = {}
dnn_cuts = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]


def get_mass_cut(mass):
    sigma_5 = 5 * (-0.0202966 + 0.0190822 * mass)
    return (mass - sigma_5, mass + sigma_5)


# prepare folders
for mass in mass_points:
    folder_path = pathlib.Path(f"m_{mass:02d}")
    folder_path.mkdir(parents=True, exist_ok=True)
    mass_cut_low, mass_cut_high = get_mass_cut(mass)
    for dnn_cut in dnn_cuts:
        dnn_label = f"{int(dnn_cut*100):02d}"
        # set nominal config
        new_config = config_temp.format(
            p_mass=mass,
            p_ntuple_path=nominal_ntuple_dir,
            p_mass_cut_low=mass_cut_low,
            p_mass_cut_high=mass_cut_high,
            p_dnn_cut=dnn_cut,
            p_dnn_cut_label=dnn_label,
        )
        # add systematic config
        sys_config = ""
        for sys_name in p4_sys_names:
        #for sys_name in ["EG_RESOLUTION_ALL__1"]:
            ntuple_path_up = f"/data/zprime/ntuples_fit/1220-sys/tree_{sys_name}up/mc16d"
            ntuple_path_down = f"/data/zprime/ntuples_fit/1220-sys/tree_{sys_name}down/mc16d"
            # sig
            sys_entry = config_p4_sys_temp.format(
                p_sys_name = sys_name[5:],
                p_sample = "Zprime",
                p_ntuple_path_up = ntuple_path_up,
                p_ntuple_path_down = ntuple_path_down,
                p_ntuple_files = f"sig_Zp{mass:03d}",
            )
            sys_config += sys_entry
            # bkg
            sys_entry = config_p4_sys_temp.format(
                p_sys_name = sys_name[5:],
                p_sample = "ZZ4l",
                p_ntuple_path_up = ntuple_path_up,
                p_ntuple_path_down = ntuple_path_down,
                p_ntuple_files = "bkg_qcd",
            )
            sys_config += sys_entry
        new_config += sys_config
        # write config
        config_name = f"m_{mass:03d}_dnn_p{dnn_label}_sys.config"
        with folder_path.joinpath(config_name).open("w", encoding="utf-8") as f:
            f.write(new_config)
    fit_script_name = "fit_all.sh"
    copyfile(f"./{fit_script_name}", folder_path.joinpath(fit_script_name))
