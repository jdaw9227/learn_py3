import yaml


class ConfigImporter:
    # class varibles are defaults

    def __init__(self, context):
        self.context = context
        self.config_type = None
        self.blank_out_settings = bool()
        result = {'added': [], 'errors': [], 'missing': []}

    def start_import(yaml_file):
        # form = self.context['form'](request.POST)
        #
        # if not form.is_valid():
        #     self.context['alert_message'] = 'ERROR: {}'.format(form.errors.as_text())
        #     return render(request, self.template, self.context)
        #
        # restaurant = request.location
        # rs = restaurant.all_children
        # rs.extend([restaurant])
        # config_yaml = sorted(config_yamls)[int(request.POST['config_yaml'])]
        config_yaml = 'games.yaml'
        # self.config_type = config_yaml_to_type[config_yaml]
        # self.blank_out_settings = request.POST.get('blank_out_settings', False)
        blank_out_settings = True
        yaml_obj = open(yaml_file, 'r')
        yaml_dict = yaml.load(yaml_obj)

        if not isinstance(yaml_dict, dict):
            context['alert_message'] = 'ERROR: Invalid Yaml Format.'
            print(self.context['alert_message'])
        else:
            print("Yaml is valid")
            print(self.context)
            # return render(request, self.template, self.context)


abc = ConfigImporter
yaml_file='games.yaml'
abc.start_import(yaml_file)
