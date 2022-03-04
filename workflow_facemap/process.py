from workflow_facemap.pipeline import fm
import warnings

warnings.filterwarnings('ignore')


def run(display_progress=True):

    populate_settings = {'display_progress': display_progress,
                         'reserve_jobs': False,
                         'suppress_errors': False}

    print('\n---- Populate imported and computed tables ----')

    # TODO: Populate the tables here

    print('\n---- Successfully completed workflow_calcium_imaging/process.py ----')


if __name__ == '__main__':
    run()
