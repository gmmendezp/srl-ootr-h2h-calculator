top32 = [
  'Marco',
  'anatomyz',
  'Nephistoss',
  'Whatthehellshappened',
  'juwk',
  'Bonooruu',
  'PhoenixFeather',
  'kayzo59',
  'mochila',
  'GSKirox',
  'Soli',
  'engineer124',
  'Glitchymon',
  'TheSaltySponge',
  'RoskaTyrant',
  'DylanMeeble',
  'mrmartin',
  'Namaha',
  'meanmido',
  'west0pher',
  'Cloudike',
  'Cola_osu',
  'Gavaroni1',
  'cfalcon',
  'JustSam',
  'kariossa',
  'Riley2w69t',
  'Xef199221',
  'MrMario7788',
  'Nek0',
  'KillerApp23',
  'earlweird'
]
values = {n: {m: [0, 0] for m in top32} for n in top32}
remove = ['bingo', 'multi', 'mw', 'triforce', 'sanity', 'freaky', 'ff weekly', 'entrance', 'bridge', 'beta', 'skull', 'beat', 'any%', 'dungeon', 'bq', 'coop', 'co-op']
# uncomment for qualifiers only
raceNumbers = [
  # '266081',
  # '266027',
  # '265907',
  # '265805',
  # '265499',
  # '265473',
  # '265253',
  # '264889',
  # '264840',
  # '264640',
  # '264493',
  # '264449',
  # '264373',
  # '264197',
  # '264081',
  # '264071'
]
# change to standingsWithFF.txt to count forfeits
standingsFile = 'standings.txt'

with open(standingsFile, 'r') as filehandle:
  standings = [line.replace('\n', '').split(';') for line in filehandle.readlines()]
  count = 0
  for row in standings:
    number = row[0].lower()
    goal = row[1].lower()
    if any(r in goal for r in remove):
      continue
    if len(raceNumbers) > 0 and not number in raceNumbers:
      continue
    s = row[2:]
    for i in range(len(s)):
      n = s[i]
      for j in range(i+1, len(s)):
        m = s[j]
        if n in top32 and m in top32:
          values[n][m][0] += 1
          values[m][n][1] += 1

  results = [['']]
  results[0].extend([n for n in top32])
  for n in top32:
    row = [n]
    for m in top32:
      if n == m:
        row.append('-')
      else:
        row.append('/'.join([str(v) for v in values[n][m]]))
    results.append(row)

  with open('results.csv', 'w') as filehandle:
    filehandle.write('\n'.join([';'.join(r) for r in results]))
