from flask import Flask, render_template



app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/views')
def views():
    return render_template('views.html')

@app.route('/graph')
def graph():
    return render_template('Graph.html')

@app.route('/TransactionCreditNov')
def TransactionCreditNov():
    return render_template('UOBPLAT/TranscationCreditNov.html')

@app.route('/TransactionCreditNovBills')
def TranscationCreditNovSpending():
    return render_template('UOBPLAT/TranscationCreditNovBills.html')

@app.route('/TranscationCreditNovHightoLow')
def TransactionCreditNovHightoLow():
    return render_template('UOBPLAT/TransactionCreditNovHightoLow.html')

@app.route('/TransactionCreditNovLowtoHigh')
def TransactionCreditNovLowtoHigh():
    return render_template('UOBPLAT/TranscationCreditNovLowtoHigh.html')

@app.route('/TransactionCreditDec')
def TranscationCreditDec():
    return render_template('UOBPLAT/TranscationCreditDec.html')

@app.route('/TransactionCreditDecBills')
def TransactionCreditDecBills():
     return render_template('UOBPLAT/TransactionCreditDecBills.html')

@app.route('/TransactionCreditDecHightoLow')
def TransactionCreditDecHightoLow():
    return render_template('UOBPLAT/TransactionCreditDecHightoLow.html')

@app.route('/TransactionCreditDecLowtoHigh')
def TransactionCreditDecLowtoHigh():
    return render_template('UOBPLAT/TransactionCreditDecLowtoHigh.html')

@app.route('/TransactionCreditJan')
def TransactionCreditJan():
    return render_template('UOBPLAT/TransactionCreditJan.html')

@app.route('/TransactionCreditJanHightoLow')
def TransactionCreditJanHightoLow():
    return render_template('UOBPLAT/TransactionCreditJanHightoLow.html')

@app.route('/TransactionCreditJanLowtoHigh')
def TransactionCreditJanLowtoHigh():
    return render_template('UOBPLAT/TransactionCreditJanLowtoHigh.html')

@app.route('/TransactionCreditJanBills')
def TransactionCreditJanBills():
    return render_template('UOBPLAT/TransactionCreditJanBills.html')

@app.route('/TransactionCreditNovOCBCPLAT')
def TransactionCreditNovOCBCPLAT():
    return render_template('OCBCPLATINUM/TranscationCreditNovOCBCPLAT.html')

@app.route('/TransactionCreditNovBillsOCBCPLAT')
def TranscationCreditNovSpendingOCBCPLAT():
    return render_template('OCBCPLATINUM/TranscationCreditNovBillsOCBCPLAT.html')

@app.route('/TranscationCreditNovHightoLowOCBCPLAT')
def TransactionCreditNovHightoLowOCBCPLAT():
    return render_template('OCBCPLATINUM/TransactionCreditNovHightoLowOCBCPLAT.html')

@app.route('/TransactionCreditNovLowtoHighOCBCPLAT')
def TransactionCreditNovLowtoHighOCBCPLAT():
    return render_template('OCBCPLATINUM/TranscationCreditNovLowtoHighOCBCPLAT.html')

@app.route('/TransactionCreditDecOCBCPLAT')
def TranscationCreditDecOCBCPLAT():
    return render_template('OCBCPLATINUM/TranscationCreditDecOCBCPLAT.html')

@app.route('/TransactionCreditDecBillsOCBCPLAT')
def TransactionCreditDecBillsOCBCPLAT():
     return render_template('OCBCPLATINUM/TransactionCreditDecBillsOCBCPLAT.html')

@app.route('/TransactionCreditDecHightoLowOCBCPLAT')
def TransactionCreditDecHightoLowOCBCPLAT():
    return render_template('OCBCPLATINUM/TransactionCreditDecHightoLowOCBCPLAT.html')

@app.route('/TransactionCreditDecLowtoHighOCBCPLAT')
def TransactionCreditDecLowtoHighOCBCPLAT():
    return render_template('OCBCPLATINUM/TransactionCreditDecLowtoHighOCBCPLAT.html')

@app.route('/TransactionCreditJanOCBCPLAT')
def TransactionCreditJanOCBCPLAT():
    return render_template('OCBCPLATINUM/TransactionCreditJanOCBCPLAT.html')

@app.route('/TransactionCreditJanHightoLowOCBCPLAT')
def TransactionCreditJanHightoLowOCBCPLAT():
    return render_template('OCBCPLATINUM/TransactionCreditJanHightoLowOCBCPLAT.html')

@app.route('/TransactionCreditJanLowtoHighOCBCPLAT')
def TransactionCreditJanLowtoHighOCBCPLAT():
    return render_template('OCBCPLATINUM/TransactionCreditJanLowtoHighOCBCPLAT.html')

@app.route('/TransactionCreditJanBillsOCBCPLAT')
def TransactionCreditJanBillsOCBCPLAT():
    return render_template('OCBCPLATINUM/TransactionCreditJanBillsOCBCPLAT.html')

@app.route('/TransactionCreditNovDBSBLACK')
def TransactionCreditNovDBSBLACK():
    transList = []
    #cardNo = '7381-3191-7122-0333'
    transList = TransactionDA.retrieveTransList()
    total = TransactionDA.calcTotalAmountByMonth(12)
    transList = TransactionDA.filterTransByMonth(12)
    #transList = TransactionDA.filterTransByDateRange('01/11/2017', '15/11/2017')
    #total = TransactionDA.calcTotalAmountByDate('01/11/2017', '15/11/2017')
    return render_template('DBSBLACK/TranscationCreditNovDBSBLACK.html', trans=transList, count=len(transList),a=total)
    #return render_template('DBSBLACK/TranscationCreditNovDBSBLACK.html', trans=transList, count=len(transList))

@app.route('/TransactionCreditNovBillsDBSBLACK')
def TranscationCreditNovSpendingDBSBLACK():
    return render_template('DBSBLACK/TranscationCreditNovBillsDBSBLACK.html')

@app.route('/TranscationCreditNovHightoLowDBSBLACK')
def TransactionCreditNovHightoLowDBSBLACK():
    return render_template('DBSBLACK/TransactionCreditNovHightoLowDBSBLACK.html')

@app.route('/TransactionCreditNovLowtoHighDBSBLACK')
def TransactionCreditNovLowtoHighDBSBLACK():
    return render_template('DBSBLACK/TranscationCreditNovLowtoHighDBSBLACK.html')

@app.route('/TransactionCreditDecDBSBLACK')
def TranscationCreditDecDBSBLACK():
    return render_template('DBSBLACK/TranscationCreditDecDBSBLACK.html')

@app.route('/TransactionCreditDecBillsDBSBLACK')
def TransactionCreditDecBillsDBSBLACK():
     return render_template('DBSBLACK/TransactionCreditDecBillsDBSBLACK.html')

@app.route('/TransactionCreditDecHightoLowDBSBLACK')
def TransactionCreditDecHightoLowDBSBLACK():
    return render_template('DBSBLACK/TransactionCreditDecHightoLowDBSBLACK.html')

@app.route('/TransactionCreditDecLowtoHighDBSBLACK')
def TransactionCreditDecLowtoHighDBSBLACK():
    return render_template('DBSBLACK/TransactionCreditDecLowtoHighDBSBLACK.html')

@app.route('/TransactionCreditJanDBSBLACK')
def TransactionCreditJanDBSBLACK():
    return render_template('DBSBLACK/TransactionCreditJanDBSBLACK.html')

@app.route('/TransactionCreditJanHightoLowDBSBLACK')
def TransactionCreditJanHightoLowDBSBLACK():
    return render_template('DBSBLACK/TransactionCreditJanHightoLowDBSBLACK.html')

@app.route('/TransactionCreditJanLowtoHighDBSBLACK')
def TransactionCreditJanLowtoHighDBSBLACK():
    return render_template('DBSBLACK/TransactionCreditJanLowtoHighDBSBLACK.html')

@app.route('/TransactionCreditJanBillsDBSBLACK')
def TransactionCreditJanBillsDBSBLACK():
    return render_template('DBSBLACK/TransactionCreditJanBillsDBSBLACK.html')

@app.route('/TransactionDebitNovFrank')
def TransactionDebitNovFrank():
    return render_template('OCBCFrank/TransactionDebitNovFrank.html')

@app.route('/TransactionDebitNovHightoLowFrank')
def TransactionDebitNovFrankHightoLowFrank():
    return render_template('OCBCFrank/TransactionDebitNovHightoLowFrank.html')

@app.route('/TransactionDebitNovLowtoHighFrank')
def TransactionDebitNovFrankLowtoHighFrank():
    return render_template('OCBCFrank/TransactionDebitNovLowtoHighFrank.html')


@app.route('/TransactionDebitNovUOBDEBIT')
def TransactionDebitNovUOBDEBIT():
    return render_template('UOBDEBIT/TransactionDebitNovUOBDEBIT.html')


@app.route('/TransactionDebitNovLowtoHighUOBDEBIT')
def TransactionDebitNovLowtoHighUOBDEBIT():
    return render_template('UOBDEBIT/TransactionDebitNovLowtoHighUOBDEBIT.html')


@app.route('/TransactionDebitNovHightoLowUOBDEBIT')
def TransactionDebitNovHightoLowUOBDEBIT():
    return render_template('UOBDEBIT/TransactionDebitNovHightoLowUOBDEBIT.html')

@app.route('/TransactionDebitNovPASSION')
def TransactionDebitNovPASSION():
    return render_template('PASSION/TransactionDebitNovPASSION.html')

@app.route('/TransactionDebitNovHightoLowPASSION')
def TransactionDebitNovHightoLowPASSION():
    return render_template('PASSION/TransactionDebitNovHightoLowPASSION.html')

@app.route('/TransactionDebitNovLowtoHighPASSION')
def TransactionDebitNovLowtoHighPASSION():
    return render_template('PASSION/TransactionDebitNovLowtoHighPASSION.html')

@app.route('/reportlostmain')
def reportlostmain():
    return render_template('/reportlostmain.html')

@app.route('/report')
def report():
    portfolioList = []
    cardnumber = []
    portfolioList = PortfolioDA.processPortfolio()
    cardnumber = TransactionDA.cardno()

    return render_template('/report.html', data=portfolioList, count=len(portfolioList),card=cardnumber)

@app.route('/Activation')
def Activation():
    return render_template('/Activation.html')
@app.route('/activationnewpage')
def activationnewpage():
    return render_template('/activationnewpage.html')
@app.route('/credit')
def credit():
    return render_template('/credit.html')

@app.route('/debit')
def debit():
    return render_template('/debit.html')

@app.route('/modal')
def modal():
    return render_template('/modal.html')
if __name__ == '__main__':
    app.run()

