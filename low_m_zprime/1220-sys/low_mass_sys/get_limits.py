import pathlib
import ROOT

for i, path in enumerate(pathlib.Path(".").rglob("**/myLimit_BLIND_CL95.root")):
    print("#" * 80)
    print(path)
    root_file = ROOT.TFile.Open(path.as_posix())
    root_tree = root_file.stats
    for entry in root_tree:
        # print("+2sigma: ", entry.exp_upperlimit_plus2)
        # print("+1sigma: ", entry.exp_upperlimit_plus1)
        # print("median: ", entry.exp_upperlimit)
        # print("-1sigma: ", entry.exp_upperlimit_minus1)
        # print("-2sigma: ", entry.exp_upperlimit_minus2)

        print(entry.exp_upperlimit_plus2)
        print(entry.exp_upperlimit_plus1)
        print(entry.exp_upperlimit)
        print(entry.exp_upperlimit_minus1)
        print(entry.exp_upperlimit_minus2)

    #if i > 3:
    #    break
