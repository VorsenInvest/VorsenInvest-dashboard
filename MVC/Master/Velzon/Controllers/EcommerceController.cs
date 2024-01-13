using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace Velzon.Controllers
{
    public class EcommerceController : Controller
    {

        [ActionName("Products")]
        public ActionResult Products()
        {
            return View();
        }


        [Route("/ecommerce/productdetails")]
        public ActionResult ProductDetails()
        {
            return View();
        }

        [ActionName("CreateProduct")]
        public ActionResult CreateProduct()
        {
            return View();
        }

        [ActionName("Orders")]
        public ActionResult Orders()
        {
            return View();
        }

        [ActionName("OrderDetails")]
        [Route("Ecommerce//ecommerce/orderdetails")]
        public ActionResult OrderDetails()
        {
            return View();
        }

        [ActionName("Customers")]
        public ActionResult Customers()
        {
            return View();
        }

        [ActionName("ShoppingCart")]
        public ActionResult ShoppingCart()
        {
            return View();
        }

        [ActionName("Checkout")]
        public ActionResult Checkout()
        {
            return View();
        }

        [ActionName("Sellers")]
        public ActionResult Sellers()
        {
            return View();
        }

        [ActionName("SellerDetails")]
        public ActionResult SellerDetails()
        {
            return View();
        }

    }
}
