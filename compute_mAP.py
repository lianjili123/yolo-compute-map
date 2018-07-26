from voc_eval import voc_eval

map_ = 0
classnames = ['door','robot','football']
for classname in classnames:

    ap = voc_eval('/home/lianji/darknet/results/{}.txt', '/home/lianji/darknet/data/VOCdevkit/VOC2007/Annotations/{}.xml', '/home/lianji/darknet/data/map_test.txt', classname, '.')
    map_ += ap
    print '%-20s' % (classname + '_ap:')+'%s' % ap

map = map_/len(classnames)
print '%-20s' % 'map:' + '%s' % map