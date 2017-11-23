# -*- encoding: utf-8 -*-

import pickle
import cPickle
from docx import Document


def test():
    doc = Document(r"D:\code\tk_bind_thirdparty_server\loan_template\dainihai_credit_card_product.docx")
    doc_bin = pickle.dumps(doc, -1)
    doc_bin1 = cPickle.dumps(doc, -1)
    with open(r"D:\code\tk_bind_thirdparty_server\loan_template\dainihai_credit_card_product1.docx", "wb") as f:
        f.write(doc_bin)
    with open(r"D:\code\tk_bind_thirdparty_server\loan_template\dainihai_credit_card_product2.docx", "wb") as f:
        f.write(doc_bin1)


if __name__ == "__main__":
    test()