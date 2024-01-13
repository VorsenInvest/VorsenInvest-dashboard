using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace Velzon.Controllers
{
    public class TasksController : Controller
    {

        [ActionName("KanbanBoard")]
        public ActionResult KanbanBoard()
        {
            return View();
        }

        [ActionName("ListView")]
        public ActionResult ListView()
        {
            return View();
        }

        [ActionName("TaskDetails")]
        public ActionResult TaskDetails()
        {
            return View();
        }

    }
}
