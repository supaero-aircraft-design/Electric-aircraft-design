# This file is part of FAST-OAD_CS23-HE : A framework for rapid Overall Aircraft Design of Hybrid
# Electric Aircraft.
# Copyright (C) 2022 ISAE-SUPAERO

import pathlib
import fastoad.api as oad

def rename_variables_for_payload_range(source_file_path: pathlib.Path):
    """
    Small helper function because payload range needs data based on the operational mission while
    for the sizing, the sizing mission is used.
    """

    op_name_to_sizing_name = {
        "data:mission:operational:climb:climb_rate:cruise_level": "data:mission:sizing:main_route:climb:climb_rate:cruise_level",
        "data:mission:operational:climb:climb_rate:sea_level": "data:mission:sizing:main_route:climb:climb_rate:sea_level",
        "data:mission:operational:climb:v_eas": "data:mission:sizing:main_route:climb:v_eas",
        "data:mission:operational:cruise:altitude": "data:mission:sizing:main_route:cruise:altitude",
        "data:mission:operational:cruise:v_tas": "data:TLAR:v_cruise",
        "data:mission:operational:descent:descent_rate": "data:mission:sizing:main_route:descent:descent_rate",
        "data:mission:operational:descent:v_eas": "data:mission:sizing:main_route:descent:v_eas",
        "data:mission:operational:initial_climb:energy": "data:mission:sizing:initial_climb:energy",
        "data:mission:operational:initial_climb:fuel": "data:mission:sizing:initial_climb:fuel",
        "data:mission:operational:payload:CG:x": "data:weight:payload:PAX:CG:x",
        "data:mission:operational:payload:mass": "data:weight:aircraft:payload",
        "data:mission:operational:range": "data:TLAR:range",
        "data:mission:operational:reserve:altitude": "data:mission:sizing:main_route:reserve:altitude",
        "data:mission:operational:reserve:duration": "data:mission:sizing:main_route:reserve:duration",
        "data:mission:operational:takeoff:energy": "data:mission:sizing:takeoff:energy",
        "data:mission:operational:takeoff:fuel": "data:mission:sizing:takeoff:fuel",
        "data:mission:operational:taxi_in:duration": "data:mission:sizing:taxi_in:duration",
        "data:mission:operational:taxi_in:speed": "data:mission:sizing:taxi_in:speed",
        "data:mission:operational:taxi_out:duration": "data:mission:sizing:taxi_out:duration",
        "data:mission:operational:taxi_out:speed": "data:mission:sizing:taxi_out:speed",
        "data:mission:operational:reserve:v_tas": "data:mission:sizing:main_route:reserve:v_tas",
    }

    datafile = oad.DataFile(source_file_path)

    for op_name, sizing_name in op_name_to_sizing_name.items():
        variable_to_add = oad.Variable(
            op_name, val=datafile[sizing_name].value, units=datafile[sizing_name].units
        )
        datafile.append(variable_to_add)

    datafile.save()