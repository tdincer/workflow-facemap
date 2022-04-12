import os
import numpy as np
import pandas as pd
from pathlib import Path
from .pipeline import subject, session, Device, fbe
from .paths import get_facemap_root_data_dir
from element_interface.utils import find_full_path


def ingest_subjects(file='./user_data/subjects.csv'):
    # -------------- Insert new "Subject" --------------
    print(file)
    print(os.getcwd())
    df = pd.read_csv(file)
    df = df[['subject', 'sex', 'subject_birth_date', 'subject_description']]

    print(f'\n---- Insert {len(df)} entry(s) into subject.Subject ----')
    subject.Subject.insert(df, skip_duplicates=True)

    print('\n---- Successfully completed ingest_subjects ----')


def ingest_sessions(file='./user_data/sessions.csv'):
    root_data_dir = get_facemap_root_data_dir()

    df = pd.read_csv(file)

    df['session_dir'] = df['file_path'].apply(lambda x: Path(x).parent.as_posix())

    df = df.sort_values(by=["subject", "session_dir"])
    df['session_id'] = pd.Categorical(df["session_datetime"])
    df['session_id'] = df["session_id"].cat.codes

    
    df['recording_id'] = pd.Categorical(df["session_dir"])
    df['recording_id'] = df["recording_id"].cat.codes

    df['recorder_id'] = pd.Categorical(df['recorder'])
    df['recorder_id'] = df['recorder_id'].cat.codes

    df['file_id'] = pd.Categorical(df['file_path'])
    df['file_id'] = df['file_id'].cat.codes

    df['facemap_task_id'] = pd.Categorical(df['proc_file'])
    df['facemap_task_id'] = df['facemap_task_id'].cat.codes

    df['task_mode'] = 'trigger'

    print(f'\n---- Insert entry(s) into session.Session ----')
    session.Session.insert(df[['subject', 'session_id', 'session_datetime']], skip_duplicates=True)

    print(f'\n---- Insert entry(s) into session.SessionDirectory ----')
    session.SessionDirectory.insert(df[['subject', 'session_id', 'session_dir']], skip_duplicates=True)

    print(f'\n---- Insert entry(s) into session.SessionDirectory ----')
    session.SessionDirectory.insert(df[['subject', 'session_id', 'session_dir']], skip_duplicates=True)
    
    print(f'\n---- Insert entry(s) into Device ----')
    Device.insert(df[['recorder_id', 'recorder']], skip_duplicates=True)

    print(f'\n---- Insert entry(s) into fbe.VideoRecording ----')
    fbe.VideoRecording.insert(df[['subject', 'session_id', 'recording_id', 'recorder_id']], skip_duplicates=True)

    fbe.VideoRecording.File.insert(df[['subject', 'session_id', 'recording_id', 'file_id', 'file_path']], skip_duplicates=True)

    fbe.FacemapTask.insert([
        dict(
            subject=j['subject'],
            session_id=j['session_id'],
            recording_id=j['recording_id'],
            facemap_task_id=j['facemap_task_id'],
            task_mode=j['task_mode'],
            facemap_params=np.load(find_full_path(get_facemap_root_data_dir(), j['proc_file']), allow_pickle=True).item()
        )
        for i, j in df.iterrows()
    ], skip_duplicates=True)

#    for no_facemap_key in (fbe.VideoRecording - fbe.FacemapTask).fetch('KEY'):