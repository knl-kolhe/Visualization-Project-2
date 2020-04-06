function updateSelectedTask(currentTask)
{
    var taskList=["task1a","task1b","task2a","task2b","task2c","task2d","task3a","task3b","task3c"]
    for(index=0;index<taskList.length;index++)
    {
        //console.log(taskList[index])
        if(taskList[index]==currentTask)
        {
            var tempStr="#"+taskList[index];
            // d3.select(tempStr)
            //     .node().classList.add("active");
            d3.select(tempStr).classed("active",true)
        }
        else
        {
            var tempStr="#"+taskList[index];
            if(d3.select(tempStr).classed("active")){
                d3.select(tempStr).classed("active",false)
            }

        }
    }

}
