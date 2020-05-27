import sys
import argparse
import covid.util as util
import configs

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Run Bayesian compartmental models.')
    parser.add_argument('place', help='place to use (e.g., US state)')
    parser.add_argument('--start', help='start date', default='2020-03-04')
    parser.add_argument('--end', help='end date', default=None)
    parser.add_argument('--prefix', help='path prefix for saving results', default='results')
    parser.add_argument('--config', help='model configuration name', default='SEIRD')
    
    args = parser.parse_args()
    print(args.config)
    print(str(dir(configs)))

    if args.config not in dir(configs):
        print(f'Invalid config: {args.config}. Options are {dir(configs)}')
        exit()

    config = getattr(configs, args.config)
        
    data = util.load_data()
    
    util.run_place(data,
                   args.place,
                   start=args.start,
                   end=args.end,
                   prefix=args.prefix,
                   model_type=config['model'],
                   T_future=0,
                   **config['args'])
