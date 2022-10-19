from ast import Raise
import os
import pathlib
import datajoint as dj


def get_facemap_root_data_dir():
    data_dir = os.getenv("FACEMAP_ROOT_DATA_DIR")

    assert data_dir is not None, "FACEMAP_ROOT_DATA_DIR is not defined!"

    if os.path.exists(data_dir):
        return pathlib.Path(data_dir)
    else:
        ValueError(
            f"{data_dir} path does not exist."
        )  # This should direct to user where to define it.


def get_facemap_video_files(recording_key):
    # Folder structure: root / subject / session / .avi (raw)
    data_dir = get_facemap_root_data_dir()

    from .pipeline import session

    sess_dir = data_dir / (session.SessionDirectory & recording_key).fetch1(
        "session_dir"
    )

    if not sess_dir.exists():
        raise FileNotFoundError(f"Session directory not found ({sess_dir})")

    video_filepaths = [fp.as_posix() for fp in sess_dir.glob("*.avi")]
    if video_filepaths:
        return video_filepaths
    else:
        raise FileNotFoundError(f"No video file found in {sess_dir}")
