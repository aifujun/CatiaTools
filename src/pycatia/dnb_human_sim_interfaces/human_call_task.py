#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dnb_human_sim_interfaces.human_task import HumanTask
from pycatia.dnb_human_sim_interfaces.worker_activity import WorkerActivity


class HumanCallTask(WorkerActivity):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DMAPSInterfaces.Activity
                |                         DNBHumanSimInterfaces.WorkerActivity
                |                             HumanCallTask
                | 
                | Interface representing xxx.
                | 
                | Role: Components that implement DNBIAHumanCallTaskActivity are
                | ...
                | 
                | Do not use the DNBIAHumanCallTaskActivity interface for such and such
                | ClassReference, Class#MethodReference, #InternalMethod...
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.human_call_task = com_object

    @property
    def called_task(self) -> HumanTask:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property CalledTask() As HumanTask (Read Only)
                | 
                |     Gets the Called Task
                | 
                |     Parameters:
                | 
                |         oHumanTask
                | 
                |     Returns:
                |         Error code of function.

        :rtype: HumanTask
        """

        return HumanTask(self.human_call_task.CalledTask)

    def set_called_task(self, i_target_task: HumanTask) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetCalledTask(HumanTask iTargetTask)
                | 
                |     Set the called task
                | 
                |     Parameters:
                | 
                |         iTargetTask
                | 
                |     Returns:
                |         E_FAIL : If the Desired Task belongs to different Manikin or there is Cyclic

        :param HumanTask i_target_task:
        :rtype: None
        """
        return self.human_call_task.SetCalledTask(i_target_task.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_called_task'
        # # vba_code = """
        # # Public Function set_called_task(human_call_task)
        # #     Dim iTargetTask (2)
        # #     human_call_task.SetCalledTask iTargetTask
        # #     set_called_task = iTargetTask
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'HumanCallTask(name="{self.name}")'
