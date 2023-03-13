class Opportunity(object):

    def __init__(self, id=None, name=None, account_name=None, close_date=None, type=None, stage=None,
                 primary_campaign_source=None, probability=None, budget_confirmed=None, amount=None,
                 discovery_completed=None, roi_analysis_completed=None, loss_reason=None, nextstep=None,
                 lead_source=None, description=None):
        self.id = id
        self.name = name
        self.account_name = account_name
        self.close_date = close_date if close_date is None else str(close_date)
        self.type = type
        self.stage = stage
        self.primary_campaign_source = primary_campaign_source
        self.probability = probability
        self.budget_confirmed = budget_confirmed
        self.amount = amount if amount is None else str(amount)
        self.discovery_completed = discovery_completed
        self.roi_analysis_completed = roi_analysis_completed
        self.loss_reason = loss_reason
        self.nextstep = nextstep
        self.lead_source = lead_source
        self.description = description
