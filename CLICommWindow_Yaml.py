import yaml

class LoadData_Yaml():
  def __init__(self, aOwner, aFile):
    with open(aFile, 'r') as file:
      ydata_ = yaml.full_load(file)
      #print(ydata_)
      print(ydata_['Version'])
      #aOwner.versions.append( aFile + ' ' + ydata_['Version'] )
      for category_ in ydata_['Categories']:
        #print(category_['name'])
        categoryValue_ = category_['value']
        parent_ = aOwner.addTop( categoryValue_, (category_['name'], "", "", category_['help']) )
        for element_ in category_['Elements']:
          #print(element_)
          #print( "%s %s" % (element_['name'], element_['value']) )
          help_ = ''
          if 'Help' in element_:
            help_ = element_['Help']
          aOwner.addChild( parent_, element_['value'], ("", "", element_['name'], help_) )
        if 'Group' in category_:
          for group_ in category_['Group']:
            help_ = ''
            if 'Help' in group_:
              help_ = group_['Help']
            parent1_ = aOwner.addGroup( parent_, ("", group_['name'], "", help_) )
            for element_ in group_['Elements']:
              #print(element_)
            #print( "%s %s" % (element_['name'], element_['value']) )
              help_ = ''
              if 'Help' in element_:
                help_ = element_['Help']
              aOwner.addChild( parent1_, element_['value'], ("", "", element_['name'], help_) )

