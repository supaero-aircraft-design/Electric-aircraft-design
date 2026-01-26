# This file is part of FAST-OAD_CS23-HE : A framework for rapid Overall Aircraft Design of Hybrid
# Electric Aircraft.
# Copyright (C) 2022 ISAE-SUPAERO

import pathlib

from fastga_he.gui.power_train_network_viewer import power_train_network_viewer

DATA_FOLDER_PATH = pathlib.Path(__file__).parent / "data"
RESULT_FOLDER_PATH = pathlib.Path(__file__).parent / "results"

if __name__ == "__main__":
    # Define path to the required files
    path_to_powertrain_description_file = pathlib.Path(DATA_FOLDER_PATH) / "hybrid_kodiak_100_scheme_B_propulsive_architecture.yml"
    path_to_network_viewer_file = pathlib.Path(RESULT_FOLDER_PATH) / "hybrid_kodiak_100_scheme_B_network_viewer.html"
    path_to_powertrain_data_file = pathlib.Path(RESULT_FOLDER_PATH) / "hybrid_kodiak_100_scheme_B_propulsion_data.csv"

    # Generate the network viewer file
    power_train_network_viewer(
        path_to_powertrain_description_file,
        path_to_network_viewer_file,
        animated_plot=True,
        orientation="LR",
        legend_position="TL",
        pt_watcher_path=path_to_powertrain_data_file
    )