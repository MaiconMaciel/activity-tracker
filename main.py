# rodar cada script checqando se deu erro ou não
from scripts import data_extract
from scripts import data_transform
from scripts import data_vis
from scripts import data_load


def runActivityTracker():
  data_extract()
  data_transform()
  data_vis()
  data_load()
  pass