"""
<name>Treetagger</name>
<description>creation de Treetagger widget</description>
<icon>path_to_icon.svg</icon>
<priority>11</priority> 
"""

# Standard imports...
import Orange
from OWWidget import *
import OWGUI


class OWTreetagger(OWWidget):
    """Orange widget for adding an integer value to the input"""
    
    # Widget settings declaration...
    settingsList = [
        'integer',
        'operation'
    ]   
    
    def __init__(self, parent=None, signalManager=None):
        """Widget creator."""
        
        OWWidget.__init__(self, parent, signalManager, wantMainArea=0)

        #----------------------------------------------------------------------
        # Channel definitions...
        self.inputs = [('Intenger', str, self.processInputData)]     
        self.outputs = [('Intenger', str)]

        #----------------------------------------------------------------------
        # Settings and other attribute initializations...
        self.integer = ""  
        self.operation = 'addition'
        self.loadSettings()
        
        self.inputData = None   # NB: not a setting.
        
        #----------------------------------------------------------------------
        # User interface...
        
        """self.optionsBox = OWGUI.widgetBox(self.controlArea, 'Options')
        OWGUI.spin(
            widget=self.optionsBox,          
            master=self, 
            value='integer',
            label='Value:', 
            callback=self.sendData,
            tooltip='Select an integer value to add to input.',
            min=0, 
            max=10, 
            step=1,
        )
        
        self.optionsBox.setDisabled(True) # --> desactive la box   /!\
        
        self.operationBox = OWGUI.widgetBox(self.controlArea, 'Operation')
        OWGUI.comboBox(
            widget = self.operationBox, 
            master = self, 
            value = "operation",
            items = ['addition', 'soustraction', 'multiplication'],
            callback=self.sendData,
            sendSelectedValue = True
        )

        """
        
        infoBox = OWGUI.widgetBox(self.controlArea, u'Info')
        self.infoLine = OWGUI.widgetLabel( # NB: using self here enables us to
                                           # access the label in other methods.
            widget=infoBox,              
            label='No input.',
        )

        self.resize(10, 10)

        self.sendData()
        
    def processInputData(self, inputData):
        """Method that processes the input data (as specified in __init__)."""
        # Store input data in attribute of this widget (so it can be accessed
        # from other methods).
        self.inputData = inputData  
        
        """
        # pour desactiver la box si pas de input !
        if inputData is None:
            self.optionsBox.setDisabled(True)
        else:
            self.optionsBox.setDisabled(False)
        """
        
        # Send data to output.
        self.sendData()
        
    def sendData(self):
        """Compute result of widget processing and send to output"""
        # Important: if input data is None, propagate this value to output...
        if self.inputData is None:
            self.infoLine.setText('No input.')
            self.send('Intenger', None)
            
        else:
            result = self.inputData 
            self.infoLine.setText(
                '%s' % (self.inputData)  # utiliser ca par la suite !!!     -->  , self.integer, result)
            )
            self.send('Intenger', result)
            
            


if __name__=='__main__':
    myApplication = QApplication(sys.argv)
    myWidget = OWTreetagger()
    myWidget.show()
    myWidget.processInputData()
    myApplication.exec_()
    
