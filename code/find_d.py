import glob
import sys
from lxml import etree
import gzip


examples = ['d', 'f', 'a']

word_tag = '{http://ilk.uvt.nl/FoLiA}w'
pos_tag = '{http://ilk.uvt.nl/FoLiA}pos'
lemma_tag = '{http://ilk.uvt.nl/FoLiA}lemma'
speech_tag = '{http://www.politicalmashup.nl}speech'
party_tag = '{http://www.politicalmashup.nl}party'

dir_in = sys.argv[1]

data_files = glob.glob('{}/*/data_folia/*.xml.gz'.format(dir_in))
for data_file in data_files:
    f = gzip.open(data_file)
    context = etree.iterparse(f, events=('end',), tag=(speech_tag),
                              huge_tree=True)

    for event, elem in context:
        if elem.tag == speech_tag:
            # find all words
            word_elems = elem.findall('.//{}'.format(word_tag))
            for w in word_elems:
                l = w.find(lemma_tag).attrib.get('class')
                if l in examples:
                    print '{} contains {}'.format(data_file, l)
    del context
    f.close()
