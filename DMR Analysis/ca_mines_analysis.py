import polars as pl
import numpy as np
import matplotlib.pyplot as plt
import geopandas

mines_csv = pl.read_csv(
    r"C:\Users\16617\Desktop\Code_Library\DMR Analysis\DMR_All_Mines.csv",
    ignore_errors=True,
)

print("Data Read")

cols_to_keep = [
    "Mine_ID",
    "MineName",
    "X",
    "Y",
    "Latitude",
    "Longitude",
    "ReportYear",
    "Acres_Dist",
    "MineStatus",
    "Operator",
    "Opt_City",
    "Owner",
    "PriProduct",
    "Other_Prod",
    "Opt_Type",
    "FaceAmount",
]

mines_csv = mines_csv[cols_to_keep]

active_mines = mines_csv.filter(pl.col("MineStatus").str.contains("ACTIVE"))

active_open_pit_mines = active_mines.filter(
    (pl.col("Opt_Type").str.contains("OPEN PIT"))
    & (~pl.col("PriProduct").str.contains("NOT REPORT"))
)

holloway = active_mines.filter(pl.col("Operator").str.contains("OLLOWA"))

counties = geopandas.read_file(
    r"C:\Users\16617\Desktop\Code_Library\DMR Analysis\ca-county-boundaries\CA_Counties\CA_Counties_TIGER2016.shp"
)

fig, ax = plt.subplots()

counties.boundary.plot(ax=ax)

sizes = (
    active_open_pit_mines.select(pl.col("FaceAmount")).fill_null(0).to_numpy().squeeze()
)
norm_sizes = 10000 * (sizes / np.linalg.norm(sizes))
labels, index = np.unique(
    active_open_pit_mines.select(pl.col("PriProduct")).to_numpy().squeeze(),
    return_inverse=True,
)

sc = ax.scatter(
    active_open_pit_mines["X"],
    active_open_pit_mines["Y"],
    s=norm_sizes,
    c=index,
    alpha=0.5,
)
ax.legend(
    sc.legend_elements(num=None)[0], labels, loc="center left", bbox_to_anchor=(1, 0.5)
)
plt.scatter(holloway["X"], holloway["Y"], c="red", label="Holloway")
plt.show()
print("Fuck")
