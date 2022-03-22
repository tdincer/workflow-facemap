import os
import pandas as pd
from .pipeline import subject, session, facial_behavior_estimation, Device
from .paths import get_facemap_root_data_dir


def ingest_subjects(file='./user_data/subjects.csv'):
    # -------------- Insert new "Subject" --------------
    print(file)
    print(os.getcwd())
    df = pd.read_csv(file)

    print(f'\n---- Insert {len(df)} entry(s) into subject.Subject ----')
    subject.Subject.insert(df, skip_duplicates=True)

    print('\n---- Successfully completed ingest_subjects ----')


def ingest_sessions(file='./user_data/sessions.csv'):
    root_data_dir = get_facemap_root_data_dir()

    df = pd.read_csv(file)

    print(f'\n---- Insert {len(df)} entry(s) into session.Session ----')
    session.Session.insert(df, skip_duplicates=True)

    print('\n---- Successfully completed ingest_sessions ----')

