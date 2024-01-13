using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace Velzon.Controllers
{
    public class CRMController : Controller
    {

        [ActionName("Contacts")]
        public ActionResult Contacts()
        {
            return View();
        }

        [ActionName("Companies")]
        public ActionResult Companies()
        {
            return View();
        }

        [ActionName("Deals")]
        public ActionResult Deals()
        {
            return View();
        }

        [ActionName("Leads")]
        public ActionResult Leads()
        {
            return View();
        }

    }
}
