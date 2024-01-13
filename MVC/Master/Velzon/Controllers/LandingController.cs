using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace Velzon.Controllers
{
    public class LandingController : Controller
    {
        public ActionResult Index()
        {
            return View();
        }
        public ActionResult NFTLanding()
        {
            return View();
        }

        public ActionResult Job()
        {
            return View();
        }
    }
}
