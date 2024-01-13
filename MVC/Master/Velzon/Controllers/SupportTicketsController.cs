using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace Velzon.Controllers
{
    public class SupportTicketsController : Controller
    {

        [ActionName("ListView")]
        public ActionResult ListView()
        {
            return View();
        }

        [ActionName("TicketDetails")]
        public ActionResult TicketDetails()
        {
            return View();
        }

    }
}
