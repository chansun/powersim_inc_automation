def createEmailTemplateUnder5000(addressee, sign_off):
    quote_email_quote_under_5000 = '''
        <html>
            <head>
            </head>
            <body>
                <p>
                    Dear {0},<br>
                    <br>
                    Thank you for your interest in PSIM. I have attached a quote based on your price inquiry.<br>
                    <br>
                    I will follow up with you in about a week to see if you have any questions, but you can always contact me before then if you do.<br>
                    <br>
                    Until then, feel free to view these links for more information on PSIM:<br>
                    <br>
                    <a href="https://t.sidekickopen79.com/s1t/c/5/f18dQhb0S7lC8dDMPbW2n0x6l2B9nMJW7t5XZs4XHqr-W5wLXTq3MhG-vW2z8MDM56dykWdTQbWj02?te=W3R5hFj4cm2zwW45SByG49RkdkW4fGB3l1JxwY5W1LDLyT45SB6dW1LDhHr43XxswW3K96C63SZ8dhW1GDK8Y49HStV1V3&si=5152997946163200&pi=32e0fdf5-570f-4888-b882-b38e1aac422d">
                        Tutorial videos
                    </a><br>
                    <a href="https://t.sidekickopen79.com/s1t/c/5/f18dQhb0S7lC8dDMPbW2n0x6l2B9nMJW7t5XZs4XHqr-W5wLXTq3MhG-vW2z8MDM56dykWdTQbWj02?te=W3R5hFj4cm2zwW45SByG49RkdkW4fGB3l1JxwY5W1LDLyT45SB6dW1Lw3rh3_-r5hf4fJf7yV3&si=5152997946163200&pi=32e0fdf5-570f-4888-b882-b38e1aac422d">
                        User Forum
                    </a><br>
                    <a href="https://t.sidekickopen79.com/s1t/c/5/f18dQhb0S7lC8dDMPbW2n0x6l2B9nMJW7t5XZs4XHqr-W5wLXTq3MhG-vW2z8MDM56dykWdTQbWj02?te=W3R5hFj4cm2zwW45SByG49RkdkW4fGB3l1JxwY5W1LDLyT45SB6dW1LDhHr43XxswW3K96BL45S_3cW3F4G5h43Tw41W4px6363ZVdqG0&si=5152997946163200&pi=32e0fdf5-570f-4888-b882-b38e1aac422d">
                        Application examples
                    </a><br>
                    <br>
                    Thank you, I look forward to hearing from you.<br>
                    <br>
                    Sincerely,<br>
                    {1}
                </p>
            </body>
        </html>
    '''.format(addressee, sign_off)
    return quote_email_quote_under_5000

def createEmailTemplateOver5000(addressee, sign_off):
    quote_email_quote_over_5000 = '''
        <html>
            <head>
            </head>
            <body>
                <p>
                    Dear {0},<br>
                    <br>
                    Thank you for your interest in PSIM.  Please find attached a quote as per your price inquiry.<br>
                    <br>
                    Keep in mind that you can always add the extra modules at a later date if you find you currently only need a few of the modules listed on the quote.<br>
                    <br>
                    For Network licenses, you may choose the number of users per line item (ie: 2 users PSIM Pro and 1 user SPICE).<br>
                    <br>
                    We also offer subscriptions with terms of 2, 6, or 12 months for the Pro version only.  I've listed the rates on the quote.<br>
                    <br>
                    **If you are interested in scheduling a complimentary web meeting to cover some relevant examples of simulations that pertain specifically to your design needs, please schedule a meeting <a href="https://t.sidekickopen79.com/s1t/c/5/f18dQhb0S7lC8dDMPbW2n0x6l2B9nMJW7t5XZs4XHqr-W5wLXTq3MhG-vW2z8MDM56dykWdTQbWj02?te=W3R5hFj4cm2zwW45VdcZ1JDY5tW3K8R4D3_Z_RVW3Qz6XD3_rhPpW3K9F8z3P6cC5W3Hcwzz43WfPhW45VdcZ1GBb-9W4fPf-t1GF-Lwn49SzG32c3&si=5152997946163200&pi=bf143a36-40ca-43e2-b468-770a1d588c7a">HERE</a>.<br>
                    <br>
                    I'd also like to offer you a free full version 30 day trial of PSIM/DSIM/SmartCtrl with all available modules and no restrictions.  If you are interested, please let me know and I'll be happy to set that up for you.<br>
                    <br>
                    In the meantime, below are links to some tutorial videos for modules I have listed on your quote:<br>
                    <a href="https://t.sidekickopen79.com/s1t/c/5/f18dQhb0S7lC8dDMPbW2n0x6l2B9nMJW7t5XZs4XHqr-W5wLXTq3MhG-vW2z8MDM56dykWdTQbWj02?te=W3R5hFj4cm2zwW45SByG49RkdkW4fGB3l1JxwY5W1LDLyT45SB6dW1LDhHr43XxswW3K96C63SZ8dhW1GDK8Y49HStVW1LxKsx1GHFstW49RLlR1GKhpbW3QyLBJ3T0QBcW41n__x4fN0gkW4fPg8749M7P4F1GJTXgmM4J1&si=5152997946163200&pi=bf143a36-40ca-43e2-b468-770a1d588c7a">
                        Getting started with PSIM
                    </a><br>
                    <a href="https://t.sidekickopen79.com/s1t/c/5/f18dQhb0S7lC8dDMPbW2n0x6l2B9nMJW7t5XZs4XHqr-W5wLXTq3MhG-vW2z8MDM56dykWdTQbWj02?te=W3R5hFj4cm2zwW45SByG49RkdkW4fGB3l1JxwY5W1LDLyT45SB6dW1LDhHr43XxswW3K96C63SZ8dhW1GDK8Y49HStVW1LxKsx1GHFstW49RLlR1GKhpbF3QyKxQmLXh1&si=5152997946163200&pi=bf143a36-40ca-43e2-b468-770a1d588c7a">
                        Getting started with DSIM
                    </a><br>
                    <a href="https://t.sidekickopen79.com/s1t/c/5/f18dQhb0S7lC8dDMPbW2n0x6l2B9nMJW7t5XZs4XHqr-W5wLXTq3MhG-vW2z8MDM56dykWdTQbWj02?te=W3R5hFj4cm2zwW45SByG49RkdkW4fGB3l1JxwY5W1LDLyT45SB6dW1LDhHr43XxswW3K96C63SZ8dhW1GDK8Y49HStVW1LxKsx4fJfX_W1GHFst49RLlRW1GKhpb3QyLBJW3T0QBy45Q2Z3W1GF7924hJ22m0&si=5152997946163200&pi=bf143a36-40ca-43e2-b468-770a1d588c7a">
                        SPICE
                    </a><br>
                    <a href="https://t.sidekickopen79.com/s1t/c/5/f18dQhb0S7lC8dDMPbW2n0x6l2B9nMJW7t5XZs4XHqr-W5wLXTq3MhG-vW2z8MDM56dykWdTQbWj02?te=W3R5hFj4cm2zwW45SByG49RkdkW4fGB3l1JxwY5W1LDLyT45SB6dW1LDhHr43XxswW3K96C63SZ8dhW1GDK8Y49HStVW1LzPRk49P7BVW4cHYRf3K2y_VW41SZYD3ZrWF8W3K2B343SYLpFW1GCtb43K8PYSW3F6bN43ZZmPc1V3&si=5152997946163200&pi=bf143a36-40ca-43e2-b468-770a1d588c7a">
                        Motor Drive
                    </a><br>
                    <a href="https://t.sidekickopen79.com/s1t/c/5/f18dQhb0S7lC8dDMPbW2n0x6l2B9nMJW7t5XZs4XHqr-W5wLXTq3MhG-vW2z8MDM56dykWdTQbWj02?te=W3R5hFj4cm2zwW45SByG49RkdkW4fGB3l1JxwY5W1LDLyT45SB6dW1LDhHr43XxswW3K96C63SZ8dhW1GDK8Y49HStVW1Lwtnm3T3QtlW1Gy-qY4fN0hvW3ZVdkV3H4TqfW3P472V3T3R3mW3H6wfV4fDXYpw3H4SPX4932&si=5152997946163200&pi=bf143a36-40ca-43e2-b468-770a1d588c7a">
                        Digital Control
                    </a><br>
                    <a href="https://t.sidekickopen79.com/s1t/c/5/f18dQhb0S7lC8dDMPbW2n0x6l2B9nMJW7t5XZs4XHqr-W5wLXTq3MhG-vW2z8MDM56dykWdTQbWj02?te=W3R5hFj4cm2zwW45SByG49RkdkW4fGB3l1JxwY5W1LDLyT45SB6dW1LDhHr43XxswW3K96C63SZ8dhW1GDK8Y49HStVW1Lyzbs49PFWfW3Fdy8c41p0ZzW3K8Qz13ZrXl7f3Hcwp3V3&si=5152997946163200&pi=bf143a36-40ca-43e2-b468-770a1d588c7a">
                        Thermal
                    </a><br>
                    <a href="https://t.sidekickopen79.com/s1t/c/5/f18dQhb0S7lC8dDMPbW2n0x6l2B9nMJW7t5XZs4XHqr-W5wLXTq3MhG-vW2z8MDM56dykWdTQbWj02?te=W3R5hFj4cm2zwW45SByG49RkdkW4fGB3l1JxwY5W1LDLyT45SB6dW1LDhHr43XxswW3K96C63SZ8dhW1GDK8Y49HStVW1Lw3q54cKKlkW3ZSzDZ43Tw4cW3LCFSm3_-qXQW41TK7V41QPRMW4cKKj_4mCW-0W1GHDvy3FbtR-f3ZVdkX04&si=5152997946163200&pi=bf143a36-40ca-43e2-b468-770a1d588c7a">
                        SimCoupler
                    </a><br>
                    <a href="https://t.sidekickopen79.com/s1t/c/5/f18dQhb0S7lC8dDMPbW2n0x6l2B9nMJW7t5XZs4XHqr-W5wLXTq3MhG-vW2z8MDM56dykWdTQbWj02?te=W3R5hFj4cm2zwW45SByG49RkdkW4fGB3l1JxwY5W1LDLyT45SB6dW1LDhHr43XxswW3K96C63SZ8dhW1GDK8Y49HStVW1LCtZm3_qtgSW41RkPX3CbGtQW3K76ZW3P8KgDw43PsGb48J2&si=5152997946163200&pi=bf143a36-40ca-43e2-b468-770a1d588c7a">
                        Renewable Energy
                    </a><br>
                    <a href="https://t.sidekickopen79.com/s1t/c/5/f18dQhb0S7lC8dDMPbW2n0x6l2B9nMJW7t5XZs4XHqr-W5wLXTq3MhG-vW2z8MDM56dykWdTQbWj02?te=W3R5hFj4cm2zwW45SByG49RkdkW4fGB3l1JxwY5W1LDLyT45SB6dW1LDhHr43XxswW3K96C63SZ8dhW1GDK8Y49HStVW1Lyz5F3ZVcXcW41YyJd3NB9bXW3K6hWD4mBcptW3K77jP3NB9RjW45LFp_43TDjTW43SH753T3R3mf45VdcZV3&si=5152997946163200&pi=bf143a36-40ca-43e2-b468-770a1d588c7a">
                        Motor Control Design Suite
                    </a><br>
                    <a href="https://t.sidekickopen79.com/s1t/c/5/f18dQhb0S7lC8dDMPbW2n0x6l2B9nMJW7t5XZs4XHqr-W5wLXTq3MhG-vW2z8MDM56dykWdTQbWj02?te=W3R5hFj4cm2zwW45SByG49RkdkW4fGB3l1JxwY5W1LDLyT45SB6dW1LDhHr43XxswW3K96C63SZ8dhW1GDK8Y49HStVW1Lyzbs49PFWfW3Fdy8c41p0wRW1GJ1Vh1GC1XRW1Gzn1f3S-qqDW4cQJHW3JF5J7W4fHLMn4cKKk10&si=5152997946163200&pi=bf143a36-40ca-43e2-b468-770a1d588c7a">
                        HEV Design Suite
                    </a><br>
                    <a href="https://t.sidekickopen79.com/s1t/c/5/f18dQhb0S7lC8dDMPbW2n0x6l2B9nMJW7t5XZs4XHqr-W5wLXTq3MhG-vW2z8MDM56dykWdTQbWj02?te=W3R5hFj4cm2zwW45SByG49RkdkW4fGB3l1JxwY5W1LDLyT45SB6dW1LDhHr43XxswW3K96C63SZ8dhW1GDK8Y49HStVW1Lyzbs49PFWfW3Fdy8c41p0ZJW1Gy80d43mx-hW3H4Mgm3K76ZWW3zhs7S41n_LkW49h9KY22VWXvW1Gzpfz1GGmmRf4fdb3_04&si=5152997946163200&pi=bf143a36-40ca-43e2-b468-770a1d588c7a">
                        SimCoder/F2833x Target
                    </a><br>
                    <a href="https://t.sidekickopen79.com/s1t/c/5/f18dQhb0S7lC8dDMPbW2n0x6l2B9nMJW7t5XZs4XHqr-W5wLXTq3MhG-vW2z8MDM56dykWdTQbWj02?te=W3R5hFj4cm2zwW45SByG49RkdkW4fGB3l1JxwY5W1LDLyT45SB6dW1LDhHr43XxswW3K96C63SZ8dhW1GDK8Y49HStVW1LxKsx1GHFstW49RLlR1GKhpbW3QyKDr3C7M4HW3K2VhS43Prd9W3P0vv149HSG3W43Tw4k4cKKqQW1GJ1Vh1GB6tFW1V2ZkQ4fDYtX4mMxp1&si=5152997946163200&pi=bf143a36-40ca-43e2-b468-770a1d588c7a">
                        SimCoder/F2837x Target
                    </a><br>
                    <a href="https://t.sidekickopen79.com/s1t/c/5/f18dQhb0S7lC8dDMPbW2n0x6l2B9nMJW7t5XZs4XHqr-W5wLXTq3MhG-vW2z8MDM56dykWdTQbWj02?te=W3R5hFj4cm2zwW45SByG49RkdkW4fGB3l1JxwY5W1LDLyT45SB6dW1LDhHr43XxswW3K96C63SZ8dhW1GDK8Y49HStVW1LCtTL3F6jXfW43W8-D41p0fNW43Vl1v3T0p5XW3T0XWM3zhs7SW41p1cQ4fHLMnW4cKKj_43XXPPW4kFl7_1GJ31bw43WgdX48R2&si=5152997946163200&pi=bf143a36-40ca-43e2-b468-770a1d588c7a">
                        PIL (Processor-In-Loop)
                    </a><br>
                    <a href="https://t.sidekickopen79.com/s1t/c/5/f18dQhb0S7lC8dDMPbW2n0x6l2B9nMJW7t5XZs4XHqr-W5wLXTq3MhG-vW2z8MDM56dykWdTQbWj02?te=W3R5hFj4cm2zwW45SByG49RkdkW4fGB3l1JxwY5W1LDLyT45SB6dW1LDhHr43XxswW3K96C63SZ8dhW1GDK8Y49HStVW1Lyzbr4fDYzRW3T1d2W49StmPW1T_Y6N47TCHcW3Xtnmv3zgF7wW45RMfB1GHD7CW4cNcDF3K9dy7W3FbtcT49PGzV0&si=5152997946163200&pi=bf143a36-40ca-43e2-b468-770a1d588c7a">
                        InstaSPIN DRV 8305
                    </a><br>
                    <a href="https://t.sidekickopen79.com/s1t/c/5/f18dQhb0S7lC8dDMPbW2n0x6l2B9nMJW7t5XZs4XHqr-W5wLXTq3MhG-vW2z8MDM56dykWdTQbWj02?te=W3R5hFj4cm2zwW45SByG49RkdkW4fGB3l1JxwY5W1LDLyT45SB6dW1LDhHr43XxswW3K96C63SZ8dhW1GDK8Y49HStVW1LFZzY3T0vWBW1GGnY_3_qtsDW4fLN6N3zd14vf3SZ8dhV3&si=5152997946163200&pi=bf143a36-40ca-43e2-b468-770a1d588c7a">
                        ModCoupler - Verilog
                    </a><br>
                    <a href="https://t.sidekickopen79.com/s1t/c/5/f18dQhb0S7lC8dDMPbW2n0x6l2B9nMJW7t5XZs4XHqr-W5wLXTq3MhG-vW2z8MDM56dykWdTQbWj02?te=W3R5hFj4cm2zwW4mKLS-4rCvX6W4hCVj23Fbt5SW4myB8V3QJdFtW2HXVz12MKHLT4n69M1&si=5152997946163200&pi=bf143a36-40ca-43e2-b468-770a1d588c7a">
                        MagCoupler
                    </a><br>
                    <a href="https://t.sidekickopen79.com/s1t/c/5/f18dQhb0S7lC8dDMPbW2n0x6l2B9nMJW7t5XZs4XHqr-W5wLXTq3MhG-vW2z8MDM56dykWdTQbWj02?te=W3R5hFj4cm2zwW45SByG49RkdkW4fGB3l1JxwY5W1LDLyT45SB6dW1LDhHr43XxswW3K96C63SZ8dhW1GDK8Y49HStVW1LDKSG49RL9FW49NjFk47TB-CW3T1McG3K2-zC4mMm51&si=5152997946163200&pi=bf143a36-40ca-43e2-b468-770a1d588c7a">
                        SmartCtrl Pro
                    </a><br>
                    <a href="https://t.sidekickopen79.com/s1t/c/5/f18dQhb0S7lC8dDMPbW2n0x6l2B9nMJW7t5XZs4XHqr-W5wLXTq3MhG-vW2z8MDM56dykWdTQbWj02?te=W3R5hFj4cm2zwW45SByG49RkdkW4fGB3l1JxwY5W1LDLyT45SB6dW1LDhHr43XxswW3K96C63SZ8dhW1GDK8Y49HStVW1LFzkr1GGnY_w3_Rx9948Q2&si=5152997946163200&pi=bf143a36-40ca-43e2-b468-770a1d588c7a">
                        PsimBook
                    </a><br>
                    <br>
                    Please let me know if you have any questions.<br>
                    <br>
                    Sincerely,<br>
                    {1}
                </p>
            </body>
        </html>
    '''.format(addressee, sign_off)
    return quote_email_quote_over_5000

def getEmailList(contact_objects):
    emails = [contact_object["properties"]["email"] for contact_object in contact_objects if contact_object["properties"]["email"] != None and contact_object["properties"]["email"] != ""]
    return emails

def getSubjectName(headerData):
    return "PSIM Quote - {0}".format(str(headerData['quote_number']))

def getAddressee(headerData):
    return headerData["prepared_for"]

def getSignOff(headerData):
    return headerData["preparer_name"]

def getRecipientEmail(contact_objects, selected_id):
    for contact_object in contact_objects:
        if contact_object["id"] == selected_id:
            return contact_object["properties"]["email"]

def getCcEmailList(contact_objects, selected_id):
    email_list = []
    for contact_object in contact_objects:
        if contact_object["id"] != selected_id:
            email_list.append(contact_object["properties"]["email"])
    email_list = ", ".join(email_list)
    return email_list