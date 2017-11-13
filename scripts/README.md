# Useful Experiment Scripts



## display_config.py

This takes in a series of comma separated pairs and prints out a nice table, that looks like the following:

### Prereq:
We use prettytable to render tables. To install, run the following

```
pip install prettytable
```


Input (test_config):

```
variable1,value1
variable2,value2
variable3,value3
variable4,value4
variable5,value5
variable6,value6
```

Output:

```
+-----------------+--------+
| Config Variable | Value  |
+-----------------+--------+
|    variable1    | value1 |
|    variable2    | value2 |
|    variable3    | value3 |
|    variable4    | value4 |
|    variable5    | value5 |
|    variable6    | value6 |
+-----------------+--------+
```

To show help message:

```
./display_config.py
```

To run:

```
./display_config.py test_config
```


## make_directory.sh

This makes a directory from the provided command line arguments and a timestamp. It will take as many arguments as you want, so go wild and crazy.

To show help message:

```
./make_directory.sh
```

To run:
```
./make_directory.sh arg1 arg2 arg3 arg4
```

Example:
I am running an experiment named test_baseline_perf and I use a weight of 20 with a buffer of 25mb and a file size of 25G. I want this reflected in my dir name.

```
./make_directory.sh test_baseline_perf weight-20 buffer-25mb fsize-25G
```

Result:

```
test_baseline_perf_weight-20_buffer-25mb_fsize-25G
```




## record_experiment.py

This makes a readme file that asks why you are running a given experiment before you proceed. This is best used as the first line in bash script so that you have to fill it out before proceeding.

To show help message:

```
./record_experiment.py
``` 

To run:

```
./record_experiment.py experiment_name
```

This will create a file named:

```
experiment_name_readme.txt
```

If you want you can provie a path and it will create a readme at that path. NOTE: Make sure you provide a path and filename like so:

```
./record_experiment.py /results/experiment_name
```

If you provide a path without a filename it will create a readme like so:

```
./record_experiment.py /results/_readme.txt
```
