ARGPARSE_ERROR_INVALID_ARGUMENTS=3
ARGPARSE_ERROR_INVALID_COMMAND=4
EMPTY_FOLDER_XML='''<com.cloudbees.hudson.plugins.folder.Folder plugin="cloudbees-folder@5.15">
<properties/>
<folderViews class="com.cloudbees.hudson.plugins.folder.views.DefaultFolderViewHolder">
<views>
<hudson.model.AllView>
<owner class="com.cloudbees.hudson.plugins.folder.Folder" reference="../../../.."/>
<name>All</name>
<filterExecutors>false</filterExecutors>
<filterQueue>false</filterQueue>
<properties class="hudson.model.View$PropertyList"/>
</hudson.model.AllView>
</views>
<tabBar class="hudson.views.DefaultViewsTabBar"/>
</folderViews>
<healthMetrics>
<com.cloudbees.hudson.plugins.folder.health.WorstChildHealthMetric>
<nonRecursive>false</nonRecursive>
</com.cloudbees.hudson.plugins.folder.health.WorstChildHealthMetric>
</healthMetrics>
<icon class="com.cloudbees.hudson.plugins.folder.icons.StockFolderIcon"/>
</com.cloudbees.hudson.plugins.folder.Folder>'''