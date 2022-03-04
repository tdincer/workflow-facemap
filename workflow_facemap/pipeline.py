import datajoint as dj
from element_lab import lab
from element_animal import subject
from element_session import session
from element_facemap import fm

from element_lab.lab import (
    Source, Lab, Protocol, User, Location, Project)
from element_animal.subject import Subject
from element_session.session_with_id import Session

from .paths import (get_fm_root_data_dir, get_video_files)


if 'custom' not in dj.config:
    dj.config['custom'] = {}

db_prefix = dj.config['custom'].get('database.prefix', '')


# ------------- Activate "lab", "subject", "session" schema -------------

lab.activate(db_prefix + 'lab')

subject.activate(db_prefix + 'subject', linking_module=__name__)

session.activate(db_prefix + 'session', linking_module=__name__)

# ------------- Declare table Device for use in element_facemap -------------

@lab.schema
class Device(dj.Manual):
    definition = """
    recorder: varchar(32) 
    """

# ------------- Activate "imaging" schema -------------
fm.activate(db_prefix + 'fm',  linking_module=__name__)