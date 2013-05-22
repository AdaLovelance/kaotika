#ifndef DIALOG_H
#define DIALOG_H

#if QT_VERSION >= 0x050000
#include <QtWidgets/QDialog>
#else
#include <QtGui/QDialog>
#endif

namespace Ui {
class Dialog;
}

class Dialog : public QDialog
{
    Q_OBJECT
    
public:
    explicit Dialog(QWidget *parent = 0);
    ~Dialog();
    
protected:
    void changeEvent(QEvent *e);
    
private:
    Ui::Dialog *ui;
};

#endif // DIALOG_H
