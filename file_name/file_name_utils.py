from os.path import basename, dirname, splitext

def getFileName(params):

  sortedParamItems = sorted(params.items(), key=lambda kv: kv[0])

  filename = 'raw_data/history/' + '&'.join(map(lambda kv: kv[0]+'='+kv[1], sortedParamItems))+'.json'

  return filename

def getParams(fileName):
  type = basename(dirname(fileName))
  base = basename(fileName)
  parts,ext = splitext(base)
  params = dict(map(lambda pair: pair.split('='), parts.split('&')))
  return {**params, 'type':type}