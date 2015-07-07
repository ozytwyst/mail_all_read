openerp.mail_all_read = function(session) {
  var _t = session.web._t,
    _lt = session.web._lt;

  var mail = session.mail;

  mail.Wall.include({

    bind_events: function(){
      this._super.apply(this, arguments);
      this.$('.oe_mail_all_read').on('click', this.mail_all_read)
    },
    mail_all_read: function(event){
      var context = {

      };
      var action = {
        type: 'ir.actions.act_window',
        res_model: 'mail_all_read.wizard',
        view_mode: 'form',
        view_type: 'form',
        views: [[false, 'form']],
        target: 'new',
        context:context
      };
      session.client.action_manager.do_action(action);
      }
  })
}
