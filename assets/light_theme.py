light = '''
<style>
    /* Main App styling */
    .stApp, .stApp .stMarkdown p, .stApp .sidebar .sidebar-content {
        background-color: #FFFFFF;
        color: #31333F;
    }

    /* Main headers styling */
    .stApp .stMarkdown h1, .stApp .stMarkdown h2 {
        color: #666666;
    }

    .stApp .stMarkdown h3 {
        color: #666666; /* Changed to a mid-gray for better visibility */
        background-color: transparent;
        margin: 0; /* Remove margin to blend seamlessly */
        padding: 0; /* Remove padding if any */
    }

    /* Sidebar headers styling */
    .stApp .sidebar .stMarkdown h1, .stApp .sidebar .stMarkdown h2 {
        color: #666666;
    }

    .stApp .sidebar .stMarkdown h3 {
        color: #666666; /* Adjusted to mid-gray for better visibility against white background */
        background-color: #FFFFFF; 
        margin: 0; /* Remove margin to blend seamlessly */
        padding: 0; /* Remove padding if any */
    }

    /* Input and text area styling */
    .stTextInput input, .stTextArea>textarea, .st-chat-inputbox {
        background-color: transparent;
        color: #31333F;
    }

    /* Button styling */
    .stButton>button {
        background-color: #FF4B4B;
        color: #31333F; /* Adjusted this for better visibility */
    }

    .stButton>button:hover {
        background-color: #E73232;
        color: #FFFFFF; /* Adjusted this for better visibility */
    }

    .stButton>button:active {
        background-color: #D62727;
        color: #FFFFFF; /* Adjusted this for better visibility */
    }

    /* Specific class with a long list of concatenated class names */
    .st-bf.st-ck.st-ek.st-el.st-em.st-en.st-cl.st-cn.st-cm.st-co.st-cp.st-b8.st-eo.st-cf.st-bm.st-e6.st-ep.st-eq.st-er.st-es.st-ae.st-af.st-ag.st-be.st-ai.st-aj.st-bx.st-et.st-eu.st-ev.st-am.st-fb {
        background-color: #FFFFFF;
        color: rgba(38, 39, 48, 0.5);
    }

    /* First class with a list of concatenated class names */
    .st-bf.st-b3.st-bl.st-eb.st-bn.st-bo.st-bp.st-bq.st-br.st-bs.st-bt.st-bu.st-ec.st-b1.st-bw.st-bh.st-bi.st-bj.st-bk.st-ed.st-ee.st-ef.st-eg.st-ck.st-eh.st-ei.st-cp {
        color: #31333F;
    }

    /* Chat input container styling */
    .stChatFloatingInputContainer.css-usj992.ehod42b2 {
        background-color: #FFFFFF;
    }

    /* Adjusting background for the specified class */
    .css-nahz7x.eqr7zpz4, .css-k7vsyb.eqr7zpz1 {
        background-color: transparent; /* Making them transparent */
        color: #31333F;
    }

    /* XPath Specific Styling */
    [id="root"] > div:nth-child(1) > div:nth-child(1) > div > div > div > section:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div > div:nth-child(3) > div > div {
        background-color: #FFFFFF;
    }

    [id="root"] > div:nth-child(1) > div:nth-child(1) > div > div > div > section:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(1) > div > div:nth-child(4) > div > div,
    [id="root"] > div:nth-child(1) > div:nth-child(1) > div > div > div > section:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(1) > div > div:nth-child(1) > div > div {
        color: #31333F;
    }

    [id="root"] > div:nth-child(1) > div:nth-child(1) > div > div > div > section:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div > div:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div > div > div > div {
        color: #31333F;
    }

    /* Other stylings remain the same ... */

</style>
'''