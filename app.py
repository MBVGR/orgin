# app.py
import streamlit as st
from streamlit.components.v1 import html as components_html

st.set_page_config(page_title="OriginFoods Preview", layout="wide")

# --- Simple session-state cart ---
if 'cart' not in st.session_state:
    # cart is dict: product_name -> {price, qty}
    st.session_state.cart = {
        "Araku Coffee — Medium Roast": {"price": 399, "qty": 0},
        "Putharekulu — Classic": {"price": 250, "qty": 0},
        "Palasa Cashew — Premium": {"price": 799, "qty": 0},
        "Kakinada Kaja — Sweet": {"price": 220, "qty": 0},
    }

# HTML strings (combined CSS + markup) for each page
home_html = """
<!doctype html>
<html lang="en">
<head><meta charset="utf-8" /><meta name="viewport" content="width=device-width,initial-scale=1" />
<style>
:root{--bg:#f7f7fb;--card:#ffffff;--muted:#6b7280;--accent:#0ea5a4;--maxw:1100px;--shadow:0 6px 18px rgba(8,15,25,0.06);font-family:Inter,system-ui,-apple-system,'Segoe UI',Roboto,'Helvetica Neue',Arial;}
*{box-sizing:border-box}html,body{height:100%}body{margin:0;background:var(--bg);color:#111827;-webkit-font-smoothing:antialiased;line-height:1.45}
.container{max-width:var(--maxw);margin:28px auto;padding:0 18px}
.header{background:var(--card);border-radius:14px;box-shadow:var(--shadow);padding:12px 18px;display:flex;align-items:center;justify-content:space-between}
.brand{display:flex;gap:12px;align-items:center}.logo{width:42px;height:42px;border-radius:10px;background:linear-gradient(135deg,var(--accent),#60d7ce);display:inline-grid;place-items:center;color:white;font-weight:700;font-size:18px;box-shadow:0 4px 12px rgba(14,165,164,0.12)}
.site-title{font-weight:700;font-size:18px}.header-links a{margin-left:14px;color:var(--muted);text-decoration:none;font-weight:600}.header-links a.cta{background:var(--accent);color:white;padding:8px 12px;border-radius:8px;text-decoration:none}
.search{margin-left:18px;flex:1;display:flex;align-items:center}.search input{width:100%;padding:10px 12px;border-radius:10px;border:1px solid #e6e9ef;background:#fbfdff;outline:none;font-size:14px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:18px;margin-top:18px}
.card{background:var(--card);border-radius:12px;padding:12px;box-shadow:var(--shadow);display:flex;flex-direction:column;gap:8px}
.card img{width:100%;height:160px;object-fit:cover;border-radius:8px}.meta{display:flex;justify-content:space-between;align-items:center}.badge{font-size:12px;background:#F0FDF4;color:#065F46;padding:6px 8px;border-radius:999px;font-weight:600}
.btn{display:inline-block;padding:10px 14px;border-radius:10px;text-decoration:none;font-weight:700}.btn.primary{background:var(--accent);color:white}
.footer{margin-top:28px;padding:18px;border-radius:12px;text-align:center;color:var(--muted)}
</style>
</head>
<body>
  <div class="container">
    <header class="header">
      <div class="brand">
        <div class="logo">OF</div>
        <div><div class="site-title">OriginFoods</div><div style="font-size:12px;color:var(--muted)">Authentic regional foods</div></div>
      </div>

      <div style="display:flex;gap:12px;align-items:center">
        <div class="search" style="max-width:420px">
          <input placeholder="Search by product or origin (Araku, Kakinada)" />
        </div>
        <nav class="header-links">
          <a href="#seller">Seller Register</a>
          <a href="#cart" class="cta">Cart</a>
        </nav>
      </div>
    </header>

    <main>
      <h2 style="margin-top:18px">Featured regional products</h2>

      <div class="grid">
        <article class="card">
          <img src="https://via.placeholder.com/600x400?text=Araku+Coffee" />
          <div class="meta"><div><div style="font-weight:700">Araku Coffee — Medium Roast</div><div style="font-size:13px;color:var(--muted)">From: Araku</div></div><div class="badge">From Araku</div></div>
          <div style="display:flex;justify-content:space-between;align-items:center;margin-top:8px"><div style="font-weight:800">₹399</div><div class="btn primary">View</div></div>
        </article>

        <article class="card">
          <img src="https://via.placeholder.com/600x400?text=Putharekulu" />
          <div class="meta"><div><div style="font-weight:700">Putharekulu — Classic</div><div style="font-size:13px;color:var(--muted)">From: Atreyapuram</div></div><div class="badge">Handmade</div></div>
          <div style="display:flex;justify-content:space-between;align-items:center;margin-top:8px"><div style="font-weight:800">₹250</div><div class="btn primary">View</div></div>
        </article>

        <article class="card">
          <img src="https://via.placeholder.com/600x400?text=Palasa+Kaju" />
          <div class="meta"><div><div style="font-weight:700">Palasa Cashew — Premium</div><div style="font-size:13px;color:var(--muted)">From: Palasa</div></div><div class="badge">From Palasa</div></div>
          <div style="display:flex;justify-content:space-between;align-items:center;margin-top:8px"><div style="font-weight:800">₹799</div><div class="btn primary">View</div></div>
        </article>

        <article class="card">
          <img src="https://via.placeholder.com/600x400?text=Kakinada+Kaja" />
          <div class="meta"><div><div style="font-weight:700">Kakinada Kaja — Sweet</div><div style="font-size:13px;color:var(--muted)">From: Kakinada</div></div><div class="badge">Local Recipe</div></div>
          <div style="display:flex;justify-content:space-between;align-items:center;margin-top:8px"><div style="font-weight:800">₹220</div><div class="btn primary">View</div></div>
        </article>

      </div>
    </main>

    <footer class="footer">© OriginFoods • Authentic products sourced directly from makers</footer>
  </div>
</body>
</html>
"""

product_html = """
<!doctype html><html lang="en"><head><meta charset="utf-8" /><meta name="viewport" content="width=device-width,initial-scale=1" />
<style>
:root{--bg:#f7f7fb;--card:#fff;--muted:#6b7280;--accent:#0ea5a4;--maxw:1100px;--shadow:0 6px 18px rgba(8,15,25,0.06);font-family:Inter,system-ui,-apple-system,'Segoe UI',Roboto,Arial;}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:#111827} .container{max-width:var(--maxw);margin:28px auto;padding:0 18px}
.header{background:var(--card);border-radius:14px;box-shadow:var(--shadow);padding:12px 18px;display:flex;align-items:center;justify-content:space-between}
.logo{width:42px;height:42px;border-radius:10px;background:linear-gradient(135deg,var(--accent),#60d7ce);display:inline-grid;place-items:center;color:white;font-weight:700}
.product-hero{display:grid;grid-template-columns:1fr 1fr;gap:20px;align-items:start;margin-top:18px}
.product-hero img{width:100%;border-radius:12px;height:420px;object-fit:cover}.product-info{background:var(--card);padding:18px;border-radius:12px;box-shadow:var(--shadow)}
.badge{font-size:12px;background:#F0FDF4;color:#065F46;padding:6px 8px;border-radius:999px;font-weight:600}.price{font-size:22px;font-weight:800;margin-top:8px}.qty{display:flex;gap:8px;align-items:center;margin-top:12px}
.btn{display:inline-block;padding:10px 14px;border-radius:10px;text-decoration:none;font-weight:700}.btn.primary{background:var(--accent);color:white}.btn.ghost{border:1px solid #e6e9ef;color:var(--muted);background:transparent}
@media (max-width:900px){.product-hero{grid-template-columns:1fr}}
</style></head><body>
<div class="container">
  <header class="header">
    <div style="display:flex;gap:12px;align-items:center"><div class="logo">OF</div><div><div style="font-weight:700">OriginFoods</div><div style="font-size:12px;color:#6b7280">Authentic regional foods</div></div></div>
    <div style="display:flex;gap:12px;align-items:center"><a href="index.html" style="color:#6b7280;text-decoration:none;margin-right:12px">Home</a><a href="cart.html" style="background:linear-gradient(90deg,#0ea5a4,#60d7ce);color:white;padding:8px 12px;border-radius:8px;text-decoration:none">Cart</a></div>
  </header>

  <main>
    <div class="product-hero">
      <div><img src="https://via.placeholder.com/900x600?text=Araku+Coffee+Bag" alt="Araku Coffee" /></div>
      <div class="product-info">
        <div style="display:flex;justify-content:space-between;align-items:center">
          <div><h1 style="margin:0">Araku Coffee — Medium Roast</h1><div style="font-size:13px;color:#6b7280">Seller: Araku Estates • From: Araku</div></div>
          <div class="badge">From Araku</div>
        </div>
        <div class="price">₹399 <span style="font-size:14px;color:#6b7280;font-weight:600">/ 250g</span></div>
        <p style="color:#6b7280;margin-top:14px">Single-origin Arabica coffee from the Araku hills. Roasted in small batches, aromatic and smooth with chocolatey notes.</p>
        <div class="qty" style="margin-top:12px"><label style="font-weight:700">Quantity</label><div style="display:flex;align-items:center;gap:8px;margin-left:8px"><div style="padding:8px 12px;border-radius:8px;border:1px solid #e6e9ef">1</div></div></div>
        <div style="margin-top:18px;display:flex;gap:12px"><div class="btn primary">Add to Cart</div><a class="btn" href="checkout.html">Buy Now</a></div>
      </div>
    </div>
  </main>

  <footer style="margin-top:28px;padding:18px;border-radius:12px;text-align:center;color:#6b7280">© OriginFoods • Origin label indicates source village/town</footer>
</div>
</body></html>
"""

seller_html = """
<!doctype html><html lang="en"><head><meta charset="utf-8" /><meta name="viewport" content="width=device-width,initial-scale=1" />
<style>
:root{--bg:#f7f7fb;--card:#fff;--muted:#6b7280;--accent:#0ea5a4;--maxw:1100px;--shadow:0 6px 18px rgba(8,15,25,0.06);font-family:Inter,system-ui,-apple-system,'Segoe UI',Roboto,Arial;}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:#111827} .container{max-width:var(--maxw);margin:28px auto;padding:0 18px}
.header{background:var(--card);border-radius:14px;box-shadow:var(--shadow);padding:12px 18px;display:flex;align-items:center;justify-content:space-between}
.logo{width:42px;height:42px;border-radius:10px;background:linear-gradient(135deg,var(--accent),#60d7ce);display:inline-grid;place-items:center;color:white;font-weight:700}
.form{background:var(--card);padding:18px;border-radius:12px;box-shadow:var(--shadow)}label{display:block;margin-bottom:6px;font-weight:700;color:#374151}input, textarea{width:100%;padding:10px;border-radius:8px;border:1px solid #e6e9ef;margin-bottom:12px}.btn{display:inline-block;padding:10px 14px;border-radius:10px;text-decoration:none;font-weight:700}.btn.primary{background:var(--accent);color:white}.aside{background:var(--card);padding:18px;border-radius:12px;box-shadow:var(--shadow)}
</style></head><body>
<div class="container">
  <header class="header"><div style="display:flex;gap:12px;align-items:center"><div class="logo">OF</div><div><div style="font-weight:700">OriginFoods</div><div style="font-size:12px;color:#6b7280">Seller onboarding</div></div></div><div><a href="index.html" style="margin-right:12px;color:#6b7280;text-decoration:none">Home</a></div></header>
  <main style="margin-top:18px">
    <div style="display:grid;grid-template-columns:1fr 360px;gap:20px">
      <div class="form"><h2 style="margin-top:0">Register as a seller</h2>
        <p style="color:#6b7280">Preview only — use the Streamlit form to submit below.</p>
      </div>
      <aside class="aside"><h3 style="margin-top:0">Seller guidelines</h3><ul style="color:#6b7280;padding-left:18px"><li>We verify origin and quality before approving.</li><li>Provide clear photos and packaging details.</li><li>Payouts are processed monthly.</li><li>Keep packaging hygienic & labeled.</li></ul></aside>
    </div>
  </main>
  <footer style="margin-top:28px;padding:18px;border-radius:12px;text-align:center;color:#6b7280">© OriginFoods • Seller registration preview</footer>
</div></body></html>
"""

cart_html = """
<!doctype html><html lang="en"><head><meta charset="utf-8" /><meta name="viewport" content="width=device-width,initial-scale=1" />
<style>
:root{--bg:#f7f7fb;--card:#fff;--muted:#6b7280;--accent:#0ea5a4;--maxw:1100px;--shadow:0 6px 18px rgba(8,15,25,0.06);font-family:Inter,system-ui,-apple-system,'Segoe UI',Roboto,Arial;}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:#111827} .container{max-width:var(--maxw);margin:28px auto;padding:0 18px}
.header{background:var(--card);border-radius:14px;box-shadow:var(--shadow);padding:12px 18px;display:flex;align-items:center;justify-content:space-between}.logo{width:42px;height:42px;border-radius:10px;background:linear-gradient(135deg,var(--accent),#60d7ce);display:inline-grid;place-items:center;color:white;font-weight:700}
.list-row{display:flex;gap:12px;align-items:center;padding:12px;border-radius:10px;background:linear-gradient(180deg,#fff,#fcfdff);border:1px solid #f1f5f9;margin-bottom:12px}.list-row img{width:92px;height:72px;object-fit:cover;border-radius:8px}
</style></head><body>
<div class="container">
  <header class="header"><div style="display:flex;gap:12px;align-items:center"><div class="logo">OF</div><div style="font-weight:700">OriginFoods</div></div><div><a href="index.html" style="color:#6b7280;text-decoration:none">Home</a></div></header>
  <main style="margin-top:18px">
    <h2>Cart</h2>
    <div class="list-row"><img src="https://via.placeholder.com/160x120?text=Araku+Coffee" alt=""><div style="flex:1"><div style="font-weight:700">Araku Coffee</div><div style="color:#6b7280;font-size:13px">250g • From Araku</div></div></div>
    <div class="list-row"><img src="https://via.placeholder.com/160x120?text=Kaja" alt=""><div style="flex:1"><div style="font-weight:700">Kakinada Kaja</div><div style="color:#6b7280;font-size:13px">Pack of 6 • From Kakinada</div></div></div>
  </main>
  <footer style="margin-top:28px;padding:18px;border-radius:12px;text-align:center;color:#6b7280">© OriginFoods</footer>
</div></body></html>
"""

checkout_html = """
<!doctype html><html lang="en"><head><meta charset="utf-8" /><meta name="viewport" content="width=device-width,initial-scale=1" />
<style>
:root{--bg:#f7f7fb;--card:#fff;--muted:#6b7280;--accent:#0ea5a4;--maxw:1100px;--shadow:0 6px 18px rgba(8,15,25,0.06);font-family:Inter,system-ui,-apple-system,'Segoe UI',Roboto,Arial;}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:#111827} .container{max-width:var(--maxw);margin:28px auto;padding:0 18px}
.header{background:var(--card);border-radius:14px;box-shadow:var(--shadow);padding:12px 18px;display:flex;align-items:center;justify-content:space-between}.logo{width:42px;height:42px;border-radius:10px;background:linear-gradient(135deg,var(--accent),#60d7ce);display:inline-grid;place-items:center;color:white;font-weight:700}
.form{background:var(--card);padding:18px;border-radius:12px;box-shadow:var(--shadow)}label{display:block;margin-bottom:6px;font-weight:700;color:#374151}input, textarea{width:100%;padding:10px;border-radius:8px;border:1px solid #e6e9ef;margin-bottom:12px}
</style></head><body>
<div class="container">
  <header class="header"><div style="display:flex;gap:12px;align-items:center"><div class="logo">OF</div><div style="font-weight:700">OriginFoods</div></div><div><a href="index.html" style="color:#6b7280;text-decoration:none">Home</a></div></header>
  <main style="margin-top:18px"><h2>Shipping & Payment</h2>
    <div class="form"><label>Full name</label><input placeholder="Name" /><label>Phone</label><input placeholder="Phone number" /><label>Address</label><textarea placeholder="House, street, landmark, city, PIN"></textarea><div style="margin-top:12px"><button style="background:linear-gradient(90deg,#0ea5a4,#60d7ce);color:white;padding:10px 14px;border-radius:10px;border:none">Place Order</button></div></div>
  </main>
  <footer style="margin-top:28px;padding:18px;border-radius:12px;text-align:center;color:#6b7280">© OriginFoods</footer>
</div></body></html>
"""

# --- Navigation ---
st.sidebar.title("OriginFoods — Preview")
page = st.sidebar.radio("Go to", ["Home", "Product", "Seller Register", "Cart", "Checkout"])

# Show small cart summary in sidebar
def cart_summary():
    total_items = sum(item['qty'] for item in st.session_state.cart.values())
    total_price = sum(item['qty'] * item['price'] for item in st.session_state.cart.values())
    st.sidebar.markdown("---")
    st.sidebar.write(f"**Cart:** {total_items} item(s)")
    st.sidebar.write(f"**Total:** ₹{total_price}")
    if st.sidebar.button("Empty cart"):
        for k in st.session_state.cart:
            st.session_state.cart[k]['qty'] = 0
        st.experimental_rerun()

cart_summary()

# --- Page rendering ---
if page == "Home":
    st.title("OriginFoods — Home (preview)")
    # embed the ready HTML; allow scrolling
    components_html(home_html, height=820, scrolling=True)
    # Provide quick add buttons below the embedded HTML
    st.markdown("### Quick add (client-side preview)")
    cols = st.columns(4)
    names = list(st.session_state.cart.keys())
    for i, col in enumerate(cols):
        name = names[i]
        with col:
            st.write(name.split("—")[0].strip())
            if st.button("Add", key=f"add_home_{i}"):
                st.session_state.cart[name]['qty'] += 1
                st.success(f"Added 1 × {name}")
                st.experimental_rerun()

elif page == "Product":
    st.title("Product — Araku Coffee (preview)")
    components_html(product_html, height=820, scrolling=True)
    # Provide a proper Add to Cart Streamlit button (real interactivity)
    if st.button("Add Araku Coffee to cart"):
        st.session_state.cart["Araku Coffee — Medium Roast"]['qty'] += 1
        st.success("Araku Coffee added to cart")
        st.experimental_rerun()

elif page == "Seller Register":
    st.title("Seller Registration (preview)")
    components_html(seller_html, height=640, scrolling=True)
    st.subheader("Submit seller info (preview form)")
    with st.form("seller_form"):
        sname = st.text_input("Full name")
        phone = st.text_input("Phone")
        shop = st.text_input("Shop / Producer name")
        city = st.text_input("City / Village")
        state = st.text_input("State")
        pincode = st.text_input("PIN code")
        desc = st.text_area("Short description of product(s)")
        submitted = st.form_submit_button("Submit registration")
    if submitted:
        st.success("Preview: seller registration captured (client-side only)")
        st.json({"name": sname, "phone": phone, "shop": shop, "city": city, "state": state, "pincode": pincode, "desc": desc})

elif page == "Cart":
    st.title("Cart (preview)")
    components_html(cart_html, height=420, scrolling=True)
    st.subheader("Your cart (client-side preview)")
    cart_items = {k: v for k, v in st.session_state.cart.items() if v['qty'] > 0}
    if not cart_items:
        st.info("Your cart is empty. Use the Product or Home page to add items.")
    else:
        for name, item in cart_items.items():
            c1, c2, c3 = st.columns([4,2,2])
            c1.write(f"**{name}**")
            c2.write(f"Qty: {item['qty']}")
            c3.write(f"₹{item['price'] * item['qty']}")
            if c3.button("Remove one", key=f"remove_{name}"):
                item['qty'] = max(0, item['qty'] - 1)
                st.experimental_rerun()
        subtotal = sum(v['price'] * v['qty'] for v in cart_items.values())
        shipping = 0 if subtotal > 499 else 49
        total = subtotal + shipping
        st.markdown("---")
        st.write(f"**Subtotal:** ₹{subtotal}")
        st.write(f"**Shipping:** ₹{shipping}")
        st.write(f"**Total:** ₹{total}")
        if st.button("Proceed to Checkout"):
            st.experimental_rerun()
elif page == "Checkout":
    st.title("Checkout (preview)")
    components_html(checkout_html, height=480, scrolling=True)
    st.subheader("Place order (preview)")
    name = st.text_input("Full name")
    phone = st.text_input("Phone")
    address = st.text_area("Address")
    payment = st.selectbox("Payment method", ["Razorpay (preview)", "UPI (preview)", "COD"])
    if st.button("Place Order"):
        if not (name and phone and address):
            st.error("Please fill name, phone and address.")
        else:
            st.success("Preview: order captured (client-side only). Check console/logs if needed.")
            st.json({"name": name, "phone": phone, "address": address, "payment": payment})
