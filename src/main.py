import sys
import argparse
import pandas

def getParser():
    parser = argparse.ArgumentParser(
        prog="AIPI510 Pre-assignment",
        description="This command line tool processes csv file in a certain way"
    )

    parser.add_argument("filename", help="String path to the csv file to process")
    parser.add_argument("--limit", type=int, default=5, help="Maximum number of rows to print during processing. Defaults to 5")
    parser.add_argument("--orig", action="store_true", help="Print the csv data before processing")
    parser.add_argument("--result", action="store_true", help="Print the csv data after processing")
    parser.add_argument("--sort", type=int, help="Sort the data by the values in the SORT column number speficied")
    parser.add_argument("--save", type=str, help="String path to the SAVE file where the processed csv data should be stored")

    return parser
    
def sort(df, sortArg):
    assert sortArg != None
    
    ascending = (sortArg > 0)
    column = df.columns[abs(sortArg) - 1]
	
    df = df.sort_values(column, ascending=ascending)
    return df

def processArgs(args):
    df = pandas.read_csv(args.filename)

    limit = max(1, args.limit)

    if args.orig:
        print("Original data:")
        print(df.head(limit))
    
    if args.sort:
        df = sort(df, args.sort)

    if args.result:
        print("Processed data:")
        print(df.head(limit))

    if args.save:
        df.to_csv(args.save, index=False)

def main(*argv):
    parser = getParser()
    args = parser.parse_args(argv[0][1:])
    processArgs(args)

if __name__ == "__main__":
    main(sys.argv)