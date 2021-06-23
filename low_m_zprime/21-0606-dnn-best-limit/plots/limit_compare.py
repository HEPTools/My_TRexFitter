import atlas_mpl_style as ampl
import matplotlib.pyplot as plt
import numpy as np

ampl.use_atlas_style(usetex=False)


mass_points = [
    5,
    7,
    9,
    11,
    13,
    15,
    17,
    19,
    23,
    27,
    31,
    35,
    39,
    42,
    45,
    48,
    51,
    54,
    57,
    60,
    63,
    66,
    69,
    72,
    75,
]
exp_limits = [
    0.002415083,
    0.002987556,
    0.00337833,
    0.003641779,
    0.003911276,
    0.004057368,
    0.00426572,
    0.004448223,
    0.004837594,
    0.0053602,
    0.006332244,
    0.007039583,
    0.008937487,
    0.012059691,
    0.013716652,
    0.017596519,
    0.023473375,
    0.029581946,
    0.040619907,
    0.057557656,
    0.084445138,
    0.125968343,
    0.188004706,
    0.255426841,
    0.308373448,
]
exp_limits_dnn = [
    0.002378545,
    0.002889704,
    0.003259255,
    0.003519453,
    0.003786972,
    0.003902442,
    0.004060433,
    0.004239164,
    0.004484654,
    0.004886385,
    0.005611997,
    0.006121026,
    0.007584023,
    0.011192193,
    0.011765344,
    0.014800446,
    0.019431214,
    0.02357105,
    0.030785777,
    0.041193328,
    0.060820734,
    0.086927826,
    0.121405585,
    0.140610679,
    0.166358368,
]

fig, ax = plt.subplots(figsize=(8.333, 8.333))

ax.plot(
    mass_points,
    exp_limits,
    color="tan",
    linestyle="-",
    label="ATLAS exp. (no DNN)",
)

ax.plot(
    mass_points,
    exp_limits_dnn,
    color="black",
    linestyle="--",
    label="ATLAS exp. (cut DNN)",
)

x = [5, 200]
y = [0.0095, 0.35]
y_high = [0.35, 0.35]
ax.plot(x, y, color="red", label="Neutrino Trident")
ax.fill_between(x, y, y_high, facecolor="red", alpha=0.2)

x = [10, 1000]
y = [0.002, 0.2]
y_low = [0.002, 0.002]
ax.plot(x, y, color="green", label="$B_s$ mixing")
ax.fill_between(x, y, y_low, facecolor="green", alpha=0.2)

ax.text(
    0.5,
    0.5,
    "$b->s\mu^+\mu^-$ anomaly \n explanation allowed",
    verticalalignment="bottom",
    horizontalalignment="left",
    rotation=45,
    transform=ax.transAxes,
    color="royalblue",
    fontsize=22,
)

ax.set_xlim(5, 1000)
ax.set_xscale("log")
ax.set_xlabel("m(Z') [GeV]")

ax.set_ylim(0.002, 0.35)
ax.set_yscale("log")
ax.set_ylabel("g")

ax.legend(loc="lower right", facecolor="white", edgecolor="black", framealpha=1.0)
ampl.plot.draw_atlas_label(
    0.05, 0.95, ax=ax, status="prelim", energy="13 TeV", lumi=139
)

fig.savefig("limit_compare.png")
fig.savefig("limit_compare.svg")
