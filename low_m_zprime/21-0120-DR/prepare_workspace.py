import pathlib
from shutil import copyfile


with open("config_template.config", "r") as f:
    config_temp = f.read()

# parameters
fit_ntup_dir = "/data/zprime/ntuples_fit/21-0120-DR"
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
    fit_script_name = "fit_all.sh"
    copyfile(f"./{fit_script_name}", folder_path_stats.joinpath(fit_script_name))

# prepare special m_42 fit mz2
mass = 42
folder_path_stats = pathlib.Path(f"high_mass_stats/m_42_mz2")
folder_path_stats.mkdir(parents=True, exist_ok=True)

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

fit_script_name = "fit_all.sh"
copyfile(f"./{fit_script_name}", folder_path_stats.joinpath(fit_script_name))


fit_script_name = "get_limits.py"
copyfile(
    f"./{fit_script_name}", pathlib.Path(f"low_mass_stats").joinpath(fit_script_name)
)
copyfile(
    f"./{fit_script_name}", pathlib.Path(f"high_mass_stats").joinpath(fit_script_name)
)
