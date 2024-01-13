using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace Velzon.Controllers
{
    public class DashBoardController : Controller
    {
        public ActionResult Index()
        {
            return View();
        }

        [ActionName("Analytics")]
        public ActionResult Analytics()
        {
            return View();
        }

        [ActionName("CRM")]
        public ActionResult CRM()
        {
            return View();
        }

        [ActionName("Crypto")]
        public ActionResult Crypto()
        {
            return View();
        }

        [ActionName("Projects")]
        public ActionResult Projects()
        {
            return View();
        }

        [ActionName("NFT")]
        public ActionResult NFT()
        {
            return View();
        }

        [ActionName("Job")]
        public ActionResult Job()
        {
            return View();
        }

    }
}
