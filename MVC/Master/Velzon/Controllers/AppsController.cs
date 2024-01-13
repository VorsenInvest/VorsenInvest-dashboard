using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace Velzon.Controllers
{
    public class AppsController : Controller
    {
        [ActionName("Calendar")]
        public ActionResult Calendar()
        {
            return View();
        }

        [ActionName("CalendarMonthGrid")]
        public ActionResult CalendarMonthGrid()
        {
            return View();
        }

        [ActionName("Chat")]
        public ActionResult Chat()
        {
            return View();
        }

        [ActionName("Mailbox")]
        public ActionResult Mailbox()
        {
            return View();
        }

        [ActionName("FileManager")]
        public ActionResult FileManager()
        {
            return View();
        }

        [ActionName("Todo")]
        public ActionResult Todo()
        {
            return View();
        }

        [ActionName("BasicAction")]
        public ActionResult BasicAction()
        {
            return View();
        }

        [ActionName("MailEcommerceAction")]
        public ActionResult MailEcommerceAction()
        {
            return View();
        }

        [ActionName("APIKey")]
        public ActionResult APIKey()
        {
            return View();
        }


    }
}
