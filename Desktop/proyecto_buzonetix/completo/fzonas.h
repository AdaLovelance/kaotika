#ifndef FZONAS_H
#define FZONAS_H

#if QT_VERSION >= 0x050000
#include <QtWidgets/QWidget>
#else
#include <QtGui/QWidget>
#endif

namespace Ui {
class fzonas;
}

class fzonas : public QWidget
{
    Q_OBJECT
    
public:
    explicit fzonas(QWidget *parent = 0);
    ~fzonas();
    
protected:
    void changeEvent(QEvent *e);
    
private:
    Ui::fzonas *ui;
};

#endif // FZONAS_H
