#include "fzonas.h"
#include "ui_fzonas.h"

fzonas::fzonas(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::fzonas)
{
    ui->setupUi(this);
}

fzonas::~fzonas()
{
    delete ui;
}

void fzonas::changeEvent(QEvent *e)
{
    QWidget::changeEvent(e);
    switch (e->type()) {
    case QEvent::LanguageChange:
        ui->retranslateUi(this);
        break;
    default:
        break;
    }
}
