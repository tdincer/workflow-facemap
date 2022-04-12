import datajoint as dj
import pathlib


def get_facemap_root_data_dir():
    data_dir = dj.config.get('custom', {}).get('facemap_root_data_dir', None)
    return pathlib.Path(data_dir) if data_dir else None


def get_facemap_video_files(recording_key):
    # Folder structure: root / subject / session / .avi (raw)
    data_dir = get_facemap_root_data_dir()

    from .pipeline import session
    sess_dir = data_dir / (session.SessionDirectory & recording_key).fetch1('session_dir')

    if not sess_dir.exists():
        raise FileNotFoundError(f'Session directory not found ({sess_dir})')

    video_filepaths = [fp.as_posix() for fp in sess_dir.glob('*.avi')]
    if video_filepaths:
        return video_filepaths
    else:
        raise FileNotFoundError(f'No video file found in {sess_dir}')
