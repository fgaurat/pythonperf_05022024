import pstats
import argparse

def main(the_file):
    p = pstats.Stats(the_file)
    # print(p.print_stats())
    p.sort_stats(pstats.SortKey.TIME).print_stats(3)


if __name__=='__main__':
    args= argparse.ArgumentParser()
    args.add_argument('the_file',help="Hoooo le fichier !")
    params = args.parse_args()
    
    main(params.the_file)
