import csv
import pathlib

import numpy as np
import ROOT
import xlwt


def get_coup_limit(mass_name, x):
    para_dict = {
        "m_05": [
            0.00014285959775009547,
            0.0030375747822960638,
            -0.0009267506934122755,
            0.0001709391854261289,
            -1.520500429564142e-05,
            5.129588006241013e-07,
        ],
        "m_07": [
            0.00017595453584282666,
            0.004506350002712834,
            -0.0019296193555482387,
            0.0005014119356643884,
            -6.288800567329947e-05,
            2.9924218006655305e-06,
        ],
        "m_09": [
            0.0002054556588638739,
            0.005968102987335838,
            -0.003208684966918542,
            0.0010498981243397564,
            -0.00016593297391993023,
            9.952291054296552e-06,
        ],
        "m_11": [
            0.00023434955540410396,
            0.007533804903872736,
            -0.004859314956131867,
            0.0019123048399373303,
            -0.000363726434025221,
            2.6260005862293543e-05,
        ],
        "m_13": [
            0.00026372453497646104,
            0.00927221893943123,
            -0.007012556831871669,
            0.0032431471878829783,
            -0.0007253313488181435,
            6.158957856185753e-05,
        ],
        "m_15": [
            0.00030140131268462095,
            0.009928707323140365,
            -0.0066873563929840596,
            0.0027497376729996767,
            -0.0005465517023259065,
            4.123766016733218e-05,
        ],
        "m_17": [
            0.00034102924027640464,
            0.010778930231433228,
            -0.006745991587815559,
            0.0025747926073592577,
            -0.0004749596227248707,
            3.325787992210886e-05,
        ],
        "m_19": [
            0.0003829175036602703,
            0.01182948238296452,
            -0.007104051922965414,
            0.002600374092165853,
            -0.00045994037888638515,
            3.087762082618056e-05,
        ],
        "m_23": [
            0.0004897939381709948,
            0.012330725436757579,
            -0.00511527756530375,
            0.0012872200675510146,
            -0.00015632526205605987,
            7.20212113738297e-06,
        ],
        "m_27": [
            0.0006125885457362561,
            0.014177661834207189,
            -0.005057743806702551,
            0.0010925494700167217,
            -0.00011385855228070985,
            4.501105148540806e-06,
        ],
        "m_31": [
            0.0007565984105016778,
            0.017291151086781597,
            -0.006016140173792976,
            0.0012671067367092646,
            -0.0001287343966321599,
            4.96102441157784e-06,
        ],
        "m_35": [
            0.0009613221073674271,
            0.01782606670819882,
            -0.0042425676872327065,
            0.0006089171088035651,
            -4.211651976156558e-05,
            1.1045069428457266e-06,
        ],
        "m_39": [
            0.0012016009128179765,
            0.020711219989254324,
            -0.004287988552453745,
            0.0005346100194725886,
            -3.2107742086009534e-05,
            7.310223187075262e-07,
        ],
        "m_42": [
            0.001413639665734382,
            0.025661920212525682,
            -0.005859087350315529,
            0.0008064572530198843,
            -5.34920003945024e-05,
            1.3453290734789734e-06,
        ],
        "m_42_mz2": [
            0.001413639665734382,
            0.025661920212525682,
            -0.005859087350315529,
            0.0008064572530198843,
            -5.34920003945024e-05,
            1.3453290734789734e-06,
        ],
        "m_45": [
            0.0016642885386911354,
            0.03242981601260141,
            -0.008434036788708524,
            0.0013240818801412155,
            -0.00010020248969094798,
            2.8754708886295387e-06,
        ],
        "m_48": [
            0.001966551519235829,
            0.0417826831724651,
            -0.012756596725438874,
            0.002354051096270498,
            -0.00020945475864435754,
            7.068112344262865e-06,
        ],
        "m_51": [
            0.0023224160441653713,
            0.0548259786981602,
            -0.020176464093835427,
            0.0044964723204448526,
            -0.00048341538776611675,
            1.9714058629911877e-05,
        ],
        "m_54": [
            0.002847330784353659,
            0.06015782161296643,
            -0.01817079334614929,
            0.003315620739819685,
            -0.0002916616710874115,
            9.729431862949621e-06,
        ],
        "m_57": [
            0.0034543530094960726,
            0.0707360500652855,
            -0.02008497570213265,
            0.00344342948855043,
            -0.00028454653591703807,
            8.915809182644659e-06,
        ],
        "m_60": [
            0.00424375697336179,
            0.07870359839248324,
            -0.018596062522632132,
            0.002648271366294158,
            -0.00018170308812117926,
            4.72598956012328e-06,
        ],
        "m_63": [
            0.005183227768423572,
            0.09311311917943178,
            -0.020787111897707888,
            0.002795867443978309,
            -0.00018125064871498723,
            4.454404106768783e-06,
        ],
        "m_66": [
            0.006256437629747566,
            0.11337448540561064,
            -0.02555348300915392,
            0.003463804281430823,
            -0.00022623427092564134,
            5.598118051902577e-06,
        ],
        "m_69": [
            0.007437009700996319,
            0.13871544818408635,
            -0.03256666852093385,
            0.004587420176565141,
            -0.0003113237247549025,
            7.997652032141912e-06,
        ],
        "m_72": [
            0.008670962916577311,
            0.16656136940447963,
            -0.04063251016443493,
            0.005931787980697107,
            -0.0004175042062685075,
            1.1116761369568317e-05,
        ],
        "m_75": [
            0.009854199243512225,
            0.1942626498410473,
            -0.04854993911222515,
            0.007224562470082335,
            -0.0005178731029686154,
            1.4011994863249172e-05,
        ],
        "m_10": [
            0.0002227282421805712,
            0.006264483507441368,
            -0.0031781875545881964,
            0.0009805232453748824,
            -0.00014609179976095968,
            8.259938550199512e-06,
        ],
    }

    p = para_dict[mass_name]
    return (
        p[0] + p[1] * x + p[2] * x ** 2 + p[3] * x ** 3 + p[4] * x ** 4 + p[5] * x ** 5
    )


data_dict = {}
for i, path in enumerate(sorted(pathlib.Path(".").rglob("**/myLimit_BLIND_CL95.root"))):
    print("#" * 80)
    print(path)
    mass = path.parts[0]
    name = path.parts[1]
    if mass not in data_dict:
        data_dict[mass] = {
            "cuts": [],
            "plus2": [],
            "plus1": [],
            "medium": [],
            "minus1": [],
            "minus2": [],
            "g_plus2": [],
            "g_plus1": [],
            "g_medium": [],
            "g_minus1": [],
            "g_minus2": [],
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

        data_dict[mass]["cuts"].append(name)
        data_dict[mass]["plus2"].append(entry.exp_upperlimit_plus2)
        data_dict[mass]["plus1"].append(entry.exp_upperlimit_plus1)
        data_dict[mass]["medium"].append(entry.exp_upperlimit)
        data_dict[mass]["minus1"].append(entry.exp_upperlimit_minus1)
        data_dict[mass]["minus2"].append(entry.exp_upperlimit_minus2)
        data_dict[mass]["g_plus2"].append(
            get_coup_limit(mass, entry.exp_upperlimit_plus2)
        )
        data_dict[mass]["g_plus1"].append(
            get_coup_limit(mass, entry.exp_upperlimit_plus1)
        )
        data_dict[mass]["g_medium"].append(get_coup_limit(mass, entry.exp_upperlimit))
        data_dict[mass]["g_minus1"].append(
            get_coup_limit(mass, entry.exp_upperlimit_minus1)
        )
        data_dict[mass]["g_minus2"].append(
            get_coup_limit(mass, entry.exp_upperlimit_minus2)
        )

print("#" * 80)
print("prepareing tables")
pathlib.Path("./csv").mkdir(parents=True, exist_ok=True)
book = xlwt.Workbook(encoding="utf-8")
best_limit_dict = dict()
raw_limit_dict = dict()
for mass, value in data_dict.items():
    rows = zip(
        value["cuts"],
        value["plus2"],
        value["plus1"],
        value["medium"],
        value["minus1"],
        value["minus2"],
        value["g_plus2"],
        value["g_plus1"],
        value["g_medium"],
        value["g_minus1"],
        value["g_minus2"],
    )
    # save csv
    with open(f"csv/{mass}.csv", "w") as file:
        writer = csv.writer(file)
        for row in rows:
            writer.writerow(row)
    # save excel
    new_sheet = book.add_sheet(mass)
    rows = zip(
        value["cuts"],
        value["plus2"],
        value["plus1"],
        value["medium"],
        value["minus1"],
        value["minus2"],
        value["g_plus2"],
        value["g_plus1"],
        value["g_medium"],
        value["g_minus1"],
        value["g_minus2"],
    )
    for row_id, row in enumerate(rows):
        for col_id, content in enumerate(row):
            new_sheet.write(col_id, row_id, content)

    best_id = np.nanargmin(value["g_medium"])
    best_limit_dict[mass] = {
        "cuts": value["cuts"][best_id],
        "plus2": value["plus2"][best_id],
        "plus1": value["plus1"][best_id],
        "medium": value["medium"][best_id],
        "minus1": value["minus1"][best_id],
        "minus2": value["minus2"][best_id],
        "g_plus2": value["g_plus2"][best_id],
        "g_plus1": value["g_plus1"][best_id],
        "g_medium": value["g_medium"][best_id],
        "g_minus1": value["g_minus1"][best_id],
        "g_minus2": value["g_minus2"][best_id],
    }
    raw_limit_dict[mass] = {
        "cuts": value["cuts"][0],
        "plus2": value["plus2"][0],
        "plus1": value["plus1"][0],
        "medium": value["medium"][0],
        "minus1": value["minus1"][0],
        "minus2": value["minus2"][0],
        "g_plus2": value["g_plus2"][0],
        "g_plus1": value["g_plus1"][0],
        "g_medium": value["g_medium"][0],
        "g_minus1": value["g_minus1"][0],
        "g_minus2": value["g_minus2"][0],
    }

# save no cut limits
new_sheet = book.add_sheet("no_cut_limits")
titles = []
for i, title in enumerate(["mass"] + list(list(raw_limit_dict.values())[0].keys())):
    new_sheet.write(i, 0, title)
for i, (mass, contents) in enumerate(raw_limit_dict.items()):
    new_sheet.write(0, i + 1, mass)
    for j, content in enumerate(contents.values()):
        new_sheet.write(j + 1, i + 1, content)

# save best limits
new_sheet = book.add_sheet("best_limits")
titles = []
for i, title in enumerate(["mass"] + list(list(best_limit_dict.values())[0].keys())):
    new_sheet.write(i, 0, title)
for i, (mass, contents) in enumerate(best_limit_dict.items()):
    new_sheet.write(0, i + 1, mass)
    for j, content in enumerate(contents.values()):
        new_sheet.write(j + 1, i + 1, content)

book.save("limits.xls")

print("#" * 80)
