import datajoint as dj
from element_lab import lab
from element_animal import subject
from element_session import session_with_id as session
from element_facemap import facial_behavior_estimation as fbe

from element_lab.lab import Source, Lab, Protocol, User, Location, Project
from element_animal.subject import Subject
from element_session.session_with_id import Session

from .paths import (get_facemap_root_data_dir, get_facemap_video_files)


if 'custom' not in dj.config:
    dj.config['custom'] = {}

db_prefix = dj.config['custom'].get('database.prefix', '')


# ------------- Activate "lab", "subject", "session" schema -------------

lab.activate(db_prefix + 'lab')

subject.activate(db_prefix + 'subject', linking_module=__name__)

Experimenter = lab.User
session.activate(db_prefix + 'session', linking_module=__name__)

# ------------- Declare table Device for use in element_facemap -------------

@lab.schema
class Device(dj.Manual):
    definition = """
    recorder_id      : smallint
    ---
    recorder         : varchar(32) 
    """

# ------------- Activate "facemap" schema -------------
fbe.activate(db_prefix + 'fm',  linking_module=__name__)
