using System.Web.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Velzon.Controllers
{
    public class InvoicesController : Controller
    {

        [ActionName("ListView")]
        public ActionResult ListView()
        {
            return View();
        }

        [ActionName("Details")]
        public ActionResult Details()
        {
            return View();
        }

        [ActionName("CreateInvoice")]
        public ActionResult CreateInvoice()
        {
            return View();
        }

    }
}
