import os

def main(directory = 'citystrides', keepdirectory = 'reduced'):
    files = os.listdir(os.path.join('data', directory))
    for filename in files:
        try:
            if not os.path.exists(os.path.join('data', keepdirectory, filename)):
                # Use -p flag below to plot the before and after, not good for large batch job.
                # os.system("python gpx_reduce.py -d 10 -n 60 -t 60 -m 200 -v 0 -p -c -2 -o "+ os.path.join('data', keepdirectory, filename) + " "+os.path.join('data', directory, filename))
                os.system("python gpx_reduce.py -d 10 -n 60 -t 60 -m 200 -v 0 -c -2 -o "+ os.path.join('data', keepdirectory, filename) + " "+os.path.join('data', directory, filename))
        except Exception as e: # work on python 3.x
            print(str(e))
            # pass

if __name__ == '__main__':
    main()
