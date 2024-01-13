using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace Velzon.Controllers
{
    public class MapsController : Controller
    {

        [ActionName("Google")]
        public ActionResult Google()
        {
            return View();
        }

        [ActionName("Vector")]
        public ActionResult Vector()
        {
            return View();
        }

        [ActionName("Leaflet")]
        public ActionResult Leaflet()
        {
            return View();
        }

    }
}
