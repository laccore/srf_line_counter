import pandas as pd
from os import scandir
from gooey import Gooey, GooeyParser
import timeit


def count_lines(input_dir, rows_to_skip):
  with scandir(input_dir) as it:
    file_list = [entry for entry in it 
                if entry.name.lower().split('.')[-1] in ['xls', 'xlsx']
                and entry.is_file()
                and not entry.name.startswith('.')]
  
  print(f'Found {len(file_list)} SRFs to count.\n')

  skip_rows = list(range(rows_to_skip))

  samples = 0

  for f in file_list:
    df = pd.read_excel(f.path, skiprows=skip_rows)
    df = df.drop_duplicates()

    samples += len(df)

    print(f'{f.name}\t{len(df)}')

  print()
  print(f'{samples} total samples collected.')


@Gooey(program_name='SRF Line Counter')
def main():
  parser = GooeyParser(description='Count the number of rows of data in a folder of SRFs for NSF reporting.')
  parser.add_argument('input_dir', default='/Users/xander/Desktop/SRFs', widget='DirChooser', metavar='Folder with SRF Excel files to evaulate', help='Path to the folder with SRFs in it')
  parser.add_argument('-s', '--rows_to_skip',
                      type=int,
                      default=8,
                      metavar='Number of rows to skip in every file',
                      help='Headers, file description, etc.',
                      gooey_options={
                        'validator':{
                            'test': 'user_input.isdigit()',
                            'message': 'Rows to skip must be a positive integer'
                        }
                      })
  args = parser.parse_args()

  start_time = timeit.default_timer()
  count_lines(args.input_dir, args.rows_to_skip)
  print(f'Completed in {round(timeit.default_timer()-start_time,2)} seconds.', flush=True)


if __name__ == '__main__':
  main()
