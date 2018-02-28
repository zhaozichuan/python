import dlg                           
import sys                              
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog     
                                        
app = QApplication(sys.argv)            
dlg = dlg.Ui_Dialog()                
qtDlg = QDialog()                       
dlg.setupUi(qtDlg)                      
qtDlg.show()                            
                                        
exit(app.exec_())                       