import csv
import pathlib

import ROOT
import xlwt

data_dict = {}
for i, path in enumerate(sorted(pathlib.Path(".").rglob("**/myLimit_BLIND_CL95.root"))):
    print("#" * 80)
    print(path)
    mass = path.parts[0]
    name = path.parts[1]
    if mass not in data_dict:
        data_dict[mass] = {
            "names": [],
            "plus2": [],
            "plus1": [],
            "medium": [],
            "minus1": [],
            "minus2": [],
        }

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

        data_dict[mass]["names"].append(name)
        data_dict[mass]["plus2"].append(entry.exp_upperlimit_plus2)
        data_dict[mass]["plus1"].append(entry.exp_upperlimit_plus1)
        data_dict[mass]["medium"].append(entry.exp_upperlimit)
        data_dict[mass]["minus1"].append(entry.exp_upperlimit_minus1)
        data_dict[mass]["minus2"].append(entry.exp_upperlimit_minus2)

print("#" * 80)
print("prepareing tables")
pathlib.Path("./csv").mkdir(parents=True, exist_ok=True)
book = xlwt.Workbook(encoding="utf-8")
for mass, value in data_dict.items():
    rows = zip(
        value["names"],
        value["plus2"],
        value["plus1"],
        value["medium"],
        value["minus1"],
        value["minus2"],
    )
    # save csv
    with open(f"csv/{mass}.csv", "w") as file:
        writer = csv.writer(file)
        for row in rows:
            writer.writerow(row)
    # save excel
    new_sheet = book.add_sheet(mass)
    rows = zip(
        value["names"],
        value["plus2"],
        value["plus1"],
        value["medium"],
        value["minus1"],
        value["minus2"],
    )
    for row_id, row in enumerate(rows):
        for col_id, content in enumerate(row):
            new_sheet.write(col_id, row_id, content)
book.save("limits.xls")
print("#" * 80)
