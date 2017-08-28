# Programming environment and tools

The course uses Python as a programming language.
It is possible to complete the assignments using any other programming language of choice. However, no support will be provided for any other programming language (hence, it is not recommended).


## 1. Python

We use Python version 3.6. It is recommended to **install the [Anaconda distribution](https://www.continuum.io/downloads) (ver 4.4.0).**

  * Python 3.5 should work just as fine, nevertheless we have only tested our code with 3.6.

### Python packages

The following packages will be used. All of these are part of the Anaconda distribution (i.e., you don't have to install them separately if you installed Anaconda).

  * `numpy`
  * `matplotlib`
  * `scikit-learn`

### Once Anaconda is installed...

...it is possible to run, in the command line, some commands installed by Anaconda. **You don't need to run them, but it is good to keep them in mind for later.** Some important commands are `conda list` (which list all the packages installed), `python`, `jupyter notebook`, `pip`.

For **Windows users**, these commands may need to be ran on the "Anaconda Prompt" instead of the standard command line prompt (cmd). You can find the Anaconda Prompt in your *Start menu*.


## 2. Elasticsearch

Elasticsearch is an open source search engine.

### 2.1. Installing Java dependencies

You will likely need to install Java dependencies before running Elasticsearch. If Java is installed, running

```
$ java -version
```

should output your Java version. Otherwise, install it:

  * Get the [latest JRE](http://www.oracle.com/technetwork/java/javase/downloads/jre8-downloads-2133155.html) (mind you need to tick the **Accept License Agreement** radio button before clicking the suitable installer);
  * install it.

Then, ensure that **its path environment variable is known by your command prompt**. For this, check that you get a correct path as output after running `where javac` on the Windows command prompt, or `whereis javac` on a Unix terminal.

If that is not known, you need to set the `JRE_HOME` environment variable, and add it to all the needed paths in the `PATH` variable.

  * On Windows, there is [a way to do it graphically](https://confluence.atlassian.com/doc/setting-the-java_home-variable-in-windows-8895.html) and, if it that doesn't work, a [way to do it on the command prompt](http://www.codejava.net/java-core/how-to-set-environment-variables-for-java-using-command-line) **running it as administrator, as explained in the link**. Mind that, in any case, you may likely need to **restart the command prompt** after the setting to check the path is right.

Even though [it claims to require JDK](https://www.elastic.co/guide/en/elasticsearch/hadoop/current/requirements.html), it should be enough to install JRE as explained. Otherwise, repeat the steps of installation (but this time installing the [latest JDK](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)) and path variable setting (but this time being `JAVA_HOME` the involved variable).

### 2.2. Installing Elasticsearch

See [this page](Elasticsearch.md) for detailed installation and usage hints. In a nutshell:

  * Download the latest [Elasticsearch distribution]( https://www.elastic.co/downloads/elasticsearch) (currently 5.5.2);
  * unzip it;
  * go to the command line (or the standard command prompt in Windows), change to the directory where Elasticsearch was unzipped (it should contain a `bin/` subdirectory);
  * run `bin/elasticsearch` on Unix, or `bin\elasticsearch.bat` on Windows.


### 2.3. Installing Python client for Elasticsearch

In addition to installing Elasticsearch, you also need to [install the Python client](Elasticsearch.md#from-python). Run:

```
pip install elasticsearch
```

in a new instance of the command line (or likely on the Anaconda prompt on Windows).



## 3. Jupyter

[Jupyter](http://jupyter.org/) is an open-source web application that allows you to run code interactively within a browser, along with visualizations, equations, and explanatory text.

Jupyter is also part of the Anaconda distribution. (If you're a Python pro and want to install it using `pip`, see [this page](http://jupyter.org/install.html).)

To start Jupyter,

  * go to a new instance of command line (or likely on the Anaconda prompt on Windows);
  * change to the directory that contains the notebooks;
  * run:

```
jupyter notebook
```

(Note that the command is `jupyter notebook`, i.e., no need to call it with the notebook file name.)

Anaconda Navigator on non-Windows installations should come with an alternative graphical launcher for Jupyter.

This will open a page on the default Web browser, where you can click on the notebook of interest.

Once in the notebook, you can run each of the cells. Mind that some cell may use a value only created if a previous cell is ran, i.e., there is some sequential relations among some cells.


## Test

Download the [Environment_test](Environment_test.ipynb) Jupyter notebook for testing if everything works.

  * Click "Raw" in the upper, right corner to download it. Make sure the extension is `.ipynb` (Windows users may experience that the Web browser only saves the file forcing a -hidden- `.txt` extension; you need to get rid of it, renaming it once [hidden extensions are shown](https://support.microsoft.com/en-us/help/865219/how-to-show-or-hide-file-name-extensions-in-windows-explorer)).
  * Go to the folder where you downloaded the file and start `jupyter notebook` as explained in the previous section.
